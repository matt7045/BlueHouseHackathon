#Sandbox.py
import alpaca_trade_api as tradeapi
import config

api = tradeapi.REST(config.alpaca.api_key, config.alpaca.secret_key, config.alpaca.paper_trade_url, api_version=config.alpaca.paper_trade_api_version)

y=api.polygon.all_tickers()
