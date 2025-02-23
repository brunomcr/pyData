from fetch_coingecko_data import fetch_coingecko_data
from save_data_to_parquet import save_data_to_parquet

def main():
    bitcoin_data = fetch_coingecko_data()
    if bitcoin_data:
        save_data_to_parquet(bitcoin_data)

if __name__ == "__main__":
    main() 