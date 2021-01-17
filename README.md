# BlueHouseHackathon

## Overview
This is a learning project, that allows for multiple different trading algorithms, to be run on multiple different makrets. This is accomplished by creating a common wrapper class for each market, implementing a common set of functions, and using those similarly-named functions in a variety of top-level trading algorithms.

## Getting Started
To fully utilize all trading algorithms/wrappers, makre sure you have the following installed:
1. **Python 3.9.x_.** Download it from https://www.python.org/downloads/
2. **KERAS Deep Learning framework.** Install it via the console command `python -m pip install Keras`. This framework is needed to run machine learning securities.
3. **An Account with Alpaca**. This brokerage offers a free paper-trading API, which is used extensively throughout the project. An account can be made for free at https://app.alpaca.markets/signup.
4. **Set up Alpaca API**. Install it via the console command `pip install alpaca-trade-api`

## Project Structure
There are three overarching sections to the project
1. Brokerage APIs
2. API Wrappers
3. Trading Algorithms

![Encapsulation Abstractions for the trading system as a whole](http://https://github.com/matt7045/BlueHouseHackathon/abstractions.PNG)

By strictly encapsulating the project's sections into these three categories, one will have the ability to use any trading algorithm, on any brokerage, so long as a API wrapper for that brokerage exists. All API wrappers must implement a "common set" of functions, that all trading algorithms know to use.

### Brokerage APIs
Brokerages all offer their own APIs to buy and sell securities. These APIs are all similar, but they have subtle differences in how they are used. All brokerage APIs that we want to use, however, should have SOME way to interact with the market by:
* Place an order to BUY a security, at a specific price
* Place an order to SELL a security, at a specific price
* View the current best BID price of a security
* View the current best ASK price of a security
Furthermore, all brokerages should have SOME way to interact with your account via methods such as:
* View your current orders
* View your current positions
* View your account balance
HOWEVER, the API endpoints you'd call to do things such as "place an order," or "view your account balance" will likely be different across APIs.

### API Wrappers
API Wrappers take the wide variety of ways that different brokerages let you interact with the markets, and reduce them down into a few "common" functions. This step is important, as it lets us use the same algorithm with different brokerage APIs. If we do not create this separation, we would have to re-write our higher-level algorithm every time we want to use it with a different brokerage! If one wishes to make an API wrapper for a brokerage, so that they can begin coding their own trading algorithm, first they must...
1. Import the MarketApiTemplate class, and all datastructure classes present, in *api_wrappers/market_api_template.py*. 
2. Create a new class for your wrapper, that inherits from MarketApiTemplate
3. Define all of the "unimplemented" methods in the template class **MarketApiTemplate**, inside of your **NEW** class
4. Import that new class in some top level algorithm file, and have some fun!
Once one creates an algorithm that makes that use that wrapper's methods, they have the freedom to run that algorithm on *any* market they want, so long as they create a wrapper in the same style for that market. 

### Trading Algorithms
**Trading Algorithms** are the "secret sauce" of the program. The **Trading Algorithms** use **API Wrappers** to communicate with the rest of the world. Doing so, allows one algorithm to work on any market that has a wrapper implemented. Algorithms will be implemented in the *trading_algorithms* folder, and can be called from a root-level **main.py** file upon completion. 
