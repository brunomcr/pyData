# pyData

# 📘 Bitcoin Historical Data Extraction

This script extracts historical price and volume data of Bitcoin using the CoinGecko API, storing the information in an Oracle database.

<p float="left">
  <img src="https://github.com/brunomcr/pyData/assets/61769161/b20f997d-6aa6-409b-a49d-081af8537abe" width="230" />
  <img src="https://github.com/brunomcr/pyData/assets/61769161/71993036-81ec-493d-9b87-b40786586a5d" width="160" /> 
  <img src="https://github.com/brunomcr/pyData/assets/61769161/c3f5b8f3-b935-4d8d-a100-41ef8755bdb4" width="70" />
</p>


### 📑 Main technologies:
```toml
cx_Oracle 8.3.0
Python 3.9
Requests 2.28.1
```

### ⚙️ Requirements
To use this script, ensure you have an API key from CoinGecko:
- Create a free account at: https://www.coingecko.com/en/api

**environment_variables.py**
* Add the following environment variables to your system or a .env file:
    ```python
    # Database credentials and host information
    DB_USER = "your_database_user"
    DB_PASSWORD = "your_database_password"
    DB_HOST = "your_database_host"
    DB_PORT = "your_database_port"
    DB_SERVICE = "your_database_service_name"

    # CoinGecko API Key
    COINGECKO_API_KEY = "your_coingecko_api_key"
    ```

### 💻 How to use:
- Clone the repository:
    ```shell
    $ git clone https://github.com/yourusername/bitcoin-historical-data.git
    $ cd bitcoin-historical-data/
    ```

- Install dependencies:
    ```shell
    $ pip install -r requirements.txt
    ```

- Run the script to extract data and save it to your Oracle database:
    ```shell
    $ python extract_and_store.py
    ```

✅ After executing the script, the Bitcoin historical data will be stored in your Oracle database under the `BTC_HISTORICO` table!

**Database Table: BTC_HISTORICO**

| Date | Price | Volume |
| ---- | ----- | ------ |
<!-- Add sample data rows here if needed -->
