class Config:
    def __init__(self):
        # Caminhos base
        self.datalake_path = "/app/data"
        self.bronze_path = f"{self.datalake_path}/bronze"
        self.silver_path = f"{self.datalake_path}/silver"
        self.gold_path = f"{self.datalake_path}/gold"

        # Caminhos Bronze
        self.bronze_path_bitcoin_data = f"{self.bronze_path}/bitcoin_data"

        # Caminhos Silver
        self.silver_path_bitcoin_data = f"{self.silver_path}/bitcoin_data"

        # Caminhos Gold
        self.gold_path_bitcoin_data = f"{self.gold_path}/bitcoin_data"
