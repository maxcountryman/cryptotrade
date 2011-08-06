##Cryptotrade

A simple API wrapper for Bitcoin trading platforms such as MtGox and TradeHill.

##Install

pip install cryptotrade

##Example

import cryptotrade

mg = cryptotrade.MtGox()
mg.ticker()

th = cryptotrade.TradeHill()
th.ticker()