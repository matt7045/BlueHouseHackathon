#Sandbox.py
import alpaca_trade_api as tradeapi

api_key_id = input("ENTER YOUR API KEY ID: ")
secret_key = input("ENTER YOUR SECRET ID:  ")
api            = tradeapi.REST(api_key_id, secret_key, 'https://paper-api.alpaca.markets', api_version='v2')

y=api.polygon.all_tickers()
