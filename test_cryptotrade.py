import unittest

import cryptotrade

class MtGoxTestCase(unittest.TestCase):
    
    def setUp(self):
        self.mg = cryptotrade.MtGox()
        self.ticker = self.mg.ticker()
        self.depth = self.mg.depth()
        self.trades = self.mg.trades()
    
    def test_public_ticker(self):
        self.assertTrue(self.ticker)
        self.assertTrue(isinstance(self.ticker, dict))
    
    def test_public_depth(self):
        self.assertTrue(self.depth)
        self.assertTrue(isinstance(self.depth, dict))
    
    def test_public_trades(self):
        self.assertTrue(self.trades)
        self.assertTrue(isinstance(self.trades, list))


class TradeHillTestCase(unittest.TestCase):

    def setUp(self):
        self.th = cryptotrade.TradeHill()
        self.ticker = self.th.ticker()
        self.trades = self.th.trades()
        self.orderbook = self.th.orderbook()
    
    def test_public_ticker(self):
        self.assertTrue(self.ticker)
        self.assertTrue(isinstance(self.ticker, dict))

    def test_public_trades(self):
        self.assertTrue(self.trades)
        self.assertTrue(isinstance(self.trades, list))

    def test_public_orderbook(self):
        self.assertTrue(self.orderbook)
        self.assertTrue(isinstance(self.orderbook, dict))
