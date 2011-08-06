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

In order to make trades with the API you'll need to provide your API token for each service. When you instantiate your instances of either platform you should provide this information. After that you're free to use all the API functionality currently offered by the platforms.

Happy trading!