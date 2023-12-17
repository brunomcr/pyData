# 📘 Bitcoin Historical Data Extraction Project

This project utilizes a Python script to extract historical Bitcoin data using the CoinGecko API. It stores this information in an Oracle database and creates interactive dashboards using Power BI for data visualization and analysis.

<div align="center">
  <table style="border-collapse: collapse; opacity: 0;">
    <tr>
      <td>
        <img src="https://github.com/brunomcr/pyData/assets/61769161/b20f997d-6aa6-409b-a49d-081af8537abe" width="230" />
      </td>
      <td>
        <img src="https://github.com/brunomcr/pyData/assets/61769161/c3f5b8f3-b935-4d8d-a100-41ef8755bdb4" width="70" />
      </td>
      <td align="center" valign="middle">
        <img src="https://github.com/brunomcr/pyData/assets/61769161/2c51c4d6-e53d-46f4-86f6-355da10a1989" width="100" />
      </td>
      <td>
        <img src="https://github.com/brunomcr/pyData/assets/61769161/71993036-81ec-493d-9b87-b40786586a5d" width="160" />
      </td>
    </tr>
  </table>
</div>

### Main Technologies by Category:

#### Data Extraction:
```
- Python 3.9
- Requests 2.28.1
```

#### Database:
```
- cx_Oracle 8.3.0
- Oracle Database
```

#### Data Visualization:
```
- Microsoft Power BI
```

### Requirements
To use this project, make sure you have a CoinGecko API key:
- Create a free account at: https://www.coingecko.com/en/api

### System Configuration
To configure the system to run the script, you need to set some environment variables. This can be done directly in the operating system or through a .env file.

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

### How to Use:
- Clone the repository:
    ```
    $ git clone https://github.com/yourusername/bitcoin-historical-data.git
    $ cd bitcoin-historical-data/
    ```

- Install dependencies:
    ```
    $ pip install -r requirements.txt
    ```

- Run the script to extract data and save it to your Oracle database:
    ```
    $ python extract_and_store.py
    ```

### Understanding the Script

The `extract_and_store.py` script performs the following steps:

1. **Configuration of Environment Variables**: It uses environment variables for Oracle database credentials and the CoinGecko API key.
2. **Connection to the Oracle Database**: It establishes a connection to the Oracle database using the provided credentials and host information.
3. **Calculation of Yesterday's Date**: It calculates the date of yesterday to use as a reference for data extraction.
4. **Conversion of Date to Unix Timestamp**: It converts the calculated date into a timestamp Unix, necessary for the request for data.
5. **Requesting Data from the CoinGecko API**: It makes a GET request to the CoinGecko API to obtain historical price and volume data of Bitcoin.
6. **Insertion of Data into the Database**: It inserts the obtained data into the `BTC_HISTORICO` table in the Oracle database.
7. **Error Handling**: In case of an error in the API request, it displays the status code and the API response.
8. **Closing Connections**: It closes the cursor and the connection to the database after data insertion.

### Running the Script

To execute the `extract_and_store.py` script, follow the steps in the 'How to Use' section above. After execution, the historical Bitcoin data will be available in the `BTC_HISTORICO` table of your Oracle database.


### Database Table
This is a screenshot of the table in the Oracle database.

<img src="https://github.com/brunomcr/pyData/assets/61769161/58e64fcc-b8a8-4054-a2df-2587349321a8" width="300"/>

### Power BI Relationship View
This screenshot shows the relationship view in Power BI, illustrating how tables are connected.

<img src="https://github.com/brunomcr/pyData/assets/61769161/3d7adf18-0777-424d-b5f0-dc625e847203" width="600"/>

### Power BI Table View
This screenshot displays a table within Power BI.

<img src="https://github.com/brunomcr/pyData/assets/61769161/e5b9a440-4728-49a0-a5e4-fa8e5af33223" width="600"/>

### Dashboard - All Years
This is a screenshot of the dashboard that provides data for all years.

<img src="https://github.com/brunomcr/pyData/assets/61769161/d00190de-e70d-47c1-b8d1-942f9e71fbc5" width="600"/>

### Dashboard - Year 2023
This screenshot represents the dashboard specifically for the year 2023.

<img src="https://github.com/brunomcr/pyData/assets/61769161/8696d73f-b849-40ef-82ee-d47159461484" width="600"/>

