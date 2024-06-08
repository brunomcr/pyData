import cx_Oracle
from pymongo import MongoClient
import os
from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


def oracle_db_connection():
    try:
        # Variáveis de Ambiente BANCO DE DADOS
        db_user = os.getenv('ORACLE_USER')
        db_password = os.getenv('ORACLE_PASSWORD')
        db_host = os.getenv('ORACLE_HOST')
        db_port = os.getenv('ORACLE_PORT')
        db_service = os.getenv('ORACLE_SERVICE')
        print('Conexao com Oracle')
        # Conexão com o banco
        return cx_Oracle.connect(f'{db_user}/{db_password}@{db_host}:{db_port}/{db_service}')
    except Exception as e:
        print('Conexão com Oracle sem sucesso\n'
              f'Erro: {e}')
        return exit(1)


def mongo_db_connection():
    # Variáveis de Ambiente BANCO DE DADOS
    mongo_user = os.getenv('MONGO_USER')
    mongo_pass = os.getenv('MONGO_PASS')
    mongo_host = os.getenv('MONGO_HOST')
    mongo_port = os.getenv('MONGO_PORT')
    db_name = os.getenv('MONGO_NAME')

    uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/"
    # uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/{db_name}?authSource=admin"
    # print(f'URI: {uri}')

    try:
        client = MongoClient(uri)
        # Try fetching the server version to confirm connection
        server_info = client.server_info()
        # print("Successfully connected to MongoDB version:", server_info['version'])
        db = client[db_name]
        print('Conexão com Mongo via Docker realizada com sucesso!')
        return db
    except Exception as e:
        print('Conexão com Mongo via Docker sem sucesso\n'
              f'Erro: {e}')
        return exit(1)

