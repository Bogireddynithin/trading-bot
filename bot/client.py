from binance.client import Client
import os
from dotenv import load_dotenv


class BinanceClient:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Get API keys
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

        # Initialize Binance client
        try:
            self.client = Client(self.api_key, self.api_secret)

            # Set Futures Testnet URL
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        except Exception as e:
            print("Error initializing Binance Client:", e)
            self.client = None

    def get_client(self):
        return self.client


# ✅ Test block (to run this file)
if __name__ == "__main__":
    bot = BinanceClient()

    if bot.get_client():
        print("✅ Client initialized successfully!")
    else:
        print("❌ Client initialization failed!")