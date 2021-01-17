#Sandbox.py
import alpaca_trade_api as tradeapi
import config

api = tradeapi.REST(config.alpaca.API_KEY, config.alpaca.SECRET_KEY, config.alpaca.PAPER_TRADE_URL, api_version=config.alpaca.PAPER_TRADE_API_VERSION)

y=api.polygon.all_tickers()
