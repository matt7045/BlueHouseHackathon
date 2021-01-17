#Sandbox.py
import config
import api_wrappers.alpaca_wrapper as api_wrapper

# Create our API wrapper from our API wrapper class
api = api_wrapper.AlpacaWrapper(config.alpaca.API_KEY, config.alpaca.SECRET_KEY)

#Use the API wrapper to get our account info
y=api.fetchAccountInfo()

#Print the info to the console!
print('Cash:         '+str(y.liquid_balance))
print('Orders:       You need to finish implementing this methods (: ')
print('Positions:    You need to finish implementing this methods (: ')
print('Total Equity: '+str(y.total_equity))
