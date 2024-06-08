from src.load_btc_data import load_data_mongodb, load_data_oracle


def main():
    load_data_mongodb()
    load_data_oracle()


if __name__ == "__main__":
    main()
