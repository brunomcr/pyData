import cx_Oracle
from pymongo import MongoClient
import os


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
    db_client = os.environ.get('MONGO_DB_CLIENT')
    db_name = os.environ.get('MONGO_DB_NAME')
    client = MongoClient(db_client)
    db = client[str(db_name)]
    print('Conexao com Mongo')
    return db
