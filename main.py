import cx_Oracle
import requests
import os
from datetime import datetime, timezone, timedelta

# Variáveis de Ambiente BANCO DE DADOS
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_SERVICE = os.environ.get('DB_SERVICE')

# Variáveis de Ambiente chave de API COINGECKO
api_key = os.environ.get('COINGECKO_API_KEY')

# Conecte-se ao banco de dados Oracle
connection = cx_Oracle.connect(f'{DB_USER}/{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SERVICE}')
cursor = connection.cursor()

# Calcule a data de ontem e de 365 dias atrás a partir de ontem
data_ontem = datetime.now(timezone.utc) - timedelta(days=1)
data_inicio = data_ontem - timedelta(days=365)

# Converta a data de início e de ontem em Unix timestamp
timestamp_inicio = int(data_inicio.timestamp())
timestamp_ontem = int(data_ontem.timestamp())

# Defina a URL da API da CoinGecko para o Bitcoin
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
params = {
    "vs_currency": "usd",
    "from": str(timestamp_inicio),
    "to": str(timestamp_ontem)
}

# Inclua a chave de API na solicitação
headers = {
    'Authorization': f'Bearer {api_key}'
}

# Faça a solicitação GET para obter os dados do histórico no intervalo de datas especificado
response = requests.get(url, params=params, headers=headers)

linhas_inseridas = 0  # Inicialize o contador de linhas inseridas

if response.status_code == 200:
    bitcoin_data = response.json()

    # Consultar a maior data presente na tabela BTC_HISTORICO_TESTE
    cursor.execute("SELECT TO_CHAR(MAX(data), 'DD-MON-YYYY') FROM BTC_HISTORICO")
    max_data_str = cursor.fetchone()[0]
    max_data = datetime.strptime(max_data_str, '%d-%b-%Y').date() if max_data_str else datetime(1970, 1, 1).date()

    for price in bitcoin_data['prices']:
        data_unix_timestamp = price[0] / 1000
        data_utc = datetime.fromtimestamp(data_unix_timestamp, timezone.utc).date()

        if data_utc > max_data:
            data_formatada = data_utc.strftime('%d-%b-%Y').upper()
            preco = price[1]
            volume = next((v[1] for v in bitcoin_data['total_volumes'] if v[0] == price[0]), 0)  # Encontra o volume correspondente

            # Insere os novos registros na tabela
            cursor.execute("INSERT INTO BTC_HISTORICO (data, preco, volume) VALUES (:data, :preco, :volume)",
                           data=data_formatada, preco=preco, volume=volume)
            linhas_inseridas += 1  # Incrementa o contador

    connection.commit()
    print(f"{linhas_inseridas} linhas foram inseridas.")  # Mostra o número de linhas inseridas
else:
    print("Erro na solicitação da API:", response.status_code, response.text)

cursor.close()
connection.close()
