from api_wrappers.market_api_template import Account
from api_wrappers.market_api_template import Order
from api_wrappers.market_api_template import Position
from api_wrappers.market_api_template import Quote

from api_wrappers.market_api_template import MarketApiTemplate
import alpaca_trade_api as tradeapi

class AlpacaWrapper(MarketApiTemplate):

    def __init__(self, api_key = 0, api_secret = 0):
        super().__init__(api_key, api_secret)
        self.api_key    = api_key
        self.api_secret = api_secret
        self.api        = tradeapi.REST(api_key, api_secret, 'https://paper-api.alpaca.markets', api_version='v2')

    #Define the function used to populate an "account" object
    def fetchAccountInfo(self):
        #Fetch the account info from the API
        account_buffer = self.api.get_account()
        order_list    = []#self.fetchOrders()
        position_list = []#self.fetchPositions()
        #Construct our Account object
        current_account = Account(  liquid_balance = account_buffer.cash,
                                    total_equity   = account_buffer.equity,
                                    orders         = order_list,
                                    positions      = position_list)
        return(current_account)

    #Define the function used to populate a list of "quotes"
    def fetchQuotes(self, symbols=[]):
        raise NotImplementedError
    #Define the function used to fetch the OPEN orders
    def fetchOrders(self):
        raise NotImplementedError
    #Define the function used to fetch current positions
    def fetchPositions(self):
        raise NotImplementedError
    #Define the function used to fetch the market hours.
    def fetchMarketHours(self):
        raise NotImplementedError
    #Define the function used to place an order
    def placeOrder(self, order):
        raise NotImplementedError
    #Define the function used to replace an order
    def replaceOrder(self, order):
        raise NotImplementedError
    #Define the function used to cancel an order
    def cancelOrder(self, order):
        raise NotImplementedError
