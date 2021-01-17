#Sandbox.py
import config
import api_wrappers.alpaca_wrapper as api_wrapper

api = api_wrapper.AlpacaWrapper(config.alpaca.API_KEY, config.alpaca.SECRET_KEY)

y=api.fetchAccountInfo()
