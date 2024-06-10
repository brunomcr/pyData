from src.load_btc_data import load_data_mongodb, load_data_oracle


def main():
    try:
        load_data_mongodb()
    except Exception as e:
        print(f"Erro ao carregar dados no MongoDB: {e}")

    try:
        load_data_oracle()
    except Exception as e:
        print(f"Erro ao carregar dados no Oracle: {e}")


if __name__ == "__main__":
    main()
