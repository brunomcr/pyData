from datetime import datetime, timezone
from src.db_connection import oracle_db_connection, mongo_db_connection
from src.fetch_coingecko_data import fetch_coingecko_data


def load_data_oracle():
    # Conexão ao banco
    connection = oracle_db_connection()
    cursor = connection.cursor()

    # Busca os dados diretamente da API Coingecko
    bitcoin_data = fetch_coingecko_data()

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
    # Conexão ao banco de dados MongoDB
    db = mongo_db_connection()

    # Seleciona ou cria a coleção 'btcHistorico' dentro do banco de dados
    collection = db['btcHistorico']
    # print(f'collection {collection}')

    # Busca os dados diretamente da API Coingecko
    bitcoin_data = fetch_coingecko_data()

    # Estrutura de retorno desejada
    result = []
    # Assegure-se de que 'prices' e 'total_volumes' têm dados correspondentes
    if 'prices' in bitcoin_data and 'total_volumes' in bitcoin_data:
        for price, volume in zip(bitcoin_data['prices'], bitcoin_data['total_volumes']):
            result.append({
                "data": datetime.fromtimestamp(price[0] / 1000),
                "preco": price[1],
                "volume": volume[1]
            })

    # Verificar a última data registrada no banco de dados
    latest_record = collection.find_one(sort=[("data", -1)])
    # print(f'latest_record {latest_record}')

    # Define a data máxima como a data do último registro ou 1º de janeiro de 1970 se não houver registros
    max_date = latest_record["data"] if latest_record else datetime(1970, 1, 1)
    # print(f'max_date {type(max_date)}')

    linhas_inseridas = 0
    for data_point in result:
        data_point_date = data_point['data']

        # Insere os novos dados que possuem uma data posterior à última registrada
        if data_point_date > max_date:
            document = {
                "data": data_point_date,
                "preco": data_point['preco'],
                "volume": data_point['volume']
            }
            collection.insert_one(document)  # Insere o documento na coleção
            linhas_inseridas += 1  # Incrementa o contador de linhas inseridas

    print(f"{linhas_inseridas} linhas foram inseridas.")  # Imprime o total de linhas inseridas
