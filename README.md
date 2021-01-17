# BlueHouseHackathon

## Overview
This is a learning project, that leverages the free Alpaca paper trading API, and Google's KERAS deep learning framework, in an attempt to classify market days as profitable, or unprofitable, dependent on data from the previous days.

## Getting Started
To get started, make sure you have:
1. **Python 3.9.x_.** Download it from https://www.python.org/downloads/
2. **KERAS Deep Learning framework.** Install it via the console command `python -m pip install Keras`. This framework is needed to run machine learning securities.
3. **An Account with Alpaca**. This brokerage offers a free paper-trading API, which is used extensively throughout the project. An account can be made for free at https://app.alpaca.markets/signup.
4. **Set up Alpaca API**. Install it via the console command `pip install alpaca-trade-api`

## Project Structure
There are three overarching sections to the project
1. Brokerage APIs
2. API Wrappers
3. Trading Algorithms

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
HOWEVER, the API endpoints you'd call to do things such as "place an order," or "view your account balance" will likely be different across APIs. API Wrappers take the 

### API Wrappers
