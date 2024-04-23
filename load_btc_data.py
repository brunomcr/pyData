import json
from datetime import datetime, timezone, timedelta
from db_connection import oracle_db_connection, mongo_db_connection
from pymongo import MongoClient
import os
from fetch_coingecko_data import fetch_coingecko_data


def load_data_oracle():
    # Conexão ao banco
    connection = oracle_db_connection()
    cursor = connection.cursor()

    # Ler dados do arquivo JSON
    with open('bitcoin_data.json', 'r') as f:
        bitcoin_data = json.load(f)

    # Verificar a última data registrada no banco
    cursor.execute("SELECT TO_CHAR(MAX(data), 'DD-MON-YYYY') FROM BTC_HISTORICO")
    max_data_str = cursor.fetchone()[0]
    max_data = datetime.strptime(max_data_str, '%d-%b-%Y').date() if max_data_str else datetime(1970, 1, 1).date()

    linhas_inseridas = 0
    for price in bitcoin_data['prices']:
        data_unix_timestamp = price[0] / 1000
        data_utc = datetime.fromtimestamp(data_unix_timestamp, timezone.utc).date()

        if data_utc > max_data:
            data_formatada = data_utc.strftime('%d-%b-%Y').upper()
            preco = price[1]
            volume = next((v[1] for v in bitcoin_data['total_volumes'] if v[0] == price[0]), 0)

            cursor.execute("INSERT INTO BTC_HISTORICO (data, preco, volume) VALUES (:data, :preco, :volume)",
                           data=data_formatada, preco=preco, volume=volume)
            linhas_inseridas += 1

    connection.commit()
    print(f"{linhas_inseridas} linhas foram inseridas.")
    cursor.close()
    connection.close()


def load_data_mongodb():
    # Conexão ao banco
    db = mongo_db_connection()
    # print(f'LISTA: {db.list_collection_names()}')
    collection = db['BTC_HISTORICO']
    print(f'collection {collection}')

    # Busca os dados diretamente da API Coingecko
    bitcoin_data = fetch_coingecko_data()

    # Verificar a última data registrada no banco
    latest_record = collection.find_one(sort=[("data", -1)])
    print(f'latest_record {latest_record}')
    max_data = latest_record["data"] if latest_record else datetime(1970, 1, 1)

    linhas_inseridas = 0
    for data_point in bitcoin_data:
        data_point_date = datetime.strptime(data_point['date'], '%Y-%m-%d')

        if data_point_date > max_data:
            document = {
                "data": data_point_date,
                "preco": data_point['price'],
                "volume": data_point['volume']
            }
            collection.insert_one(document)
            linhas_inseridas += 1

    print(f"{linhas_inseridas} linhas foram inseridas.")

