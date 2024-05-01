import cx_Oracle
from pymongo import MongoClient
import os
from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


def oracle_db_connection():
    # Variáveis de Ambiente BANCO DE DADOS
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_service = os.environ.get('DB_SERVICE')
    print('Conexao com Oracle')
    # Conexão com o banco
    return cx_Oracle.connect(f'{db_user}/{db_password}@{db_host}:{db_port}/{db_service}')

def mongo_db_connection():
    # Variáveis de Ambiente BANCO DE DADOS
    mongo_user = os.environ.get('MONGO_USER')
    mongo_pass = os.environ.get('MONGO_PASS')
    mongo_host = os.environ.get('MONGO_HOST')
    mongo_port = os.environ.get('MONGO_PORT')
    db_name = os.environ.get('MONGO_NAME')

    uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/"
    client = MongoClient(uri)
    db = client[db_name]
    print('Conexão com Mongo via Docker realizada com sucesso!')
    return db
