# All trading algorithms will use the functions defined in this
# template file to interact with their respective markets. This
# allows one trading algorithm to be used across multiple different
# markets, so long as a proper template file exists. Just define
# the following fundamental functions, and you are good.

#The following fundamental data structures will be populated with data from
# the API

# An order has the following attributes
#   id
#   direction
#   price
#   quantity
class Order:
    def __init__(self,
                 order_id  = '',
                 direction = '',
                 price     = 0,
                 quantity  = 0):
        self.order_id  = order_id
        self.direction = direction
        self.price     = price
        self.quantity  = quantity

# A position has the following attributes
#   symbol
#   direction
#   quantity
class Position:
    def __init__(self,
                 symbol         = '',
                 long_quantity  = 0,
                 short_quantity = 0):
        self.symbol          = symbol
        self.long_quantity   = long_quantity
        self.short_quantity  = short_quantity

# A quote has the following attributes
#   symbol
#   bidPrice
#   bidSize
#   askPrice
#   askSize
class Quote:
    def __init__(self,
                 symbol    = ''
                 bid_price = 0
                 bid_size  = 0
                 ask_price = 0
                 ask_size  = 0):
        self.symbol    = symbol
        self.bid_price = bid_price
        self.bid_size  = bid_size
        self.ask_price = ask_price
        self.ask_size  = ask_size

# An account has the following attributes
#   liquid balance
#   total equity
#   orders
#   positions
class Account:
    def __init__(self,
                 liquid_balance = 0,
                 total_equity   = 0,
                 orders         = [],
                 positions      = []):
        self.liquid_balance = liquid_balance
        self.total_equity   = total_equity
        self.orders         = orders
        self.positions      = positions

# A market APIoffers the following services:
#   fetch account info
#   fetch quotes
#   fetch orders
#   fetch positions
#   fetch market hours
#   place   order
#   replace orders
#   cancel  orders
"""
class MarketApi():
    def __init__(self, api_key = 0, api_secret = 0):
        self.api_key    = api_key
        self.api_secret = api_secret
    #Define the function used to populate an "account" object
    def fetchAccountInfo(self):
        raise NotImplementedError
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
