import cx_Oracle
import requests
import os
from datetime import datetime, timezone, timedelta

# Variaveis de Ambiente BANCO DE DADOS
DB_USER=os.environ.get('DB_USER')
DB_PASSWORD=os.environ.get('DB_PASSWORD')
DB_HOST=os.environ.get('DB_HOST')
DB_PORT=os.environ.get('DB_PORT')
DB_SERVICE=os.environ.get('DB_SERVICE')

# Variaveis de Ambiente chave de API COINGECKO
api_key = os.environ.get('COINGECKO_API_KEY')

# Conecte-se ao banco de dados Oracle
connection = cx_Oracle.connect(f'{DB_USER}/{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SERVICE}')

# Calcule a data de ontem
data_ontem = datetime.now(timezone.utc) - timedelta(days=1)

# Converta a data de ontem em Unix timestamp
timestamp_ontem = int(data_ontem.timestamp())

# Defina a URL da API da CoinGecko para o Bitcoin com todo o intervalo disponível
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
params = {
    "vs_currency": "usd",
    "from": "0",  # Use o valor mínimo (0) para obter os dados mais antigos
    "to": timestamp_ontem  # Data de término em formato Unix timestamp (ontem)
}

# Inclua a chave de API na solicitação
headers = {
    'Authorization': f'Bearer {api_key}'
}

# Faça a solicitação GET para obter os dados do histórico no intervalo de datas especificado
response = requests.get(url, params=params, headers=headers)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    bitcoin_data = response.json()

    # Estabeleça uma conexão com o banco de dados
    cursor = connection.cursor()

    # Acesse os campos "prices" e "total_volumes" no JSON
    prices = bitcoin_data['prices']
    total_volumes = bitcoin_data['total_volumes']

    # Inserir os dados na tabela
    cursor.execute("TRUNCATE TABLE BTC_HISTORICO ")

    # Insira os dados na tabela do banco de dados
    for i in range(len(prices)):
        data_unix_timestamp = prices[i][0] / 1000
        data_utc = datetime.fromtimestamp(data_unix_timestamp, timezone.utc)
        data_formatada = data_utc.strftime('%d-%b-%Y').upper()  # Formate a data como "DD-MON-AAAA" e converta para maiúsculas
        preco = prices[i][1]
        volume = total_volumes[i][1]

        # Inserir os dados na tabela
        cursor.execute("INSERT INTO BTC_HISTORICO (data, preco, volume) VALUES (:data, :preco, :volume)",
                       data=data_formatada, preco=preco, volume=volume)

    # Confirme a transação e feche o cursor
    connection.commit()
    cursor.close()

    # Feche a conexão com o banco de dados
    connection.close()

else:
    print("Erro na solicitação da API:")
    print(f"Status Code: {response.status_code}")
    print(f"Resposta: {response.text}")
