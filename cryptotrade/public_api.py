class MtGoxPublic(object):
    '''Public API methods for mtgox.com; provides various metrics about the 
    market status.
    '''
    
    def _set_url(self, path='data/'):
        url = self.url_base + path
        return url
    
    def ticker(self):
        return self.api_request(self._set_url() + 'ticker.php')
    
    def depth(self):
        return self.api_request(self._set_url() + 'getDepth.php')
    
    def trades(self):
        return self.api_request(self._set_url() + 'getTrades.php')


class TradeHillPublic(object):
    '''Public API methods for tradehill.com; provides various metrics about the 
    market status.
    '''
    
    def ticker(self):
        return self.api_request(self.url_base + 'Ticker')
    
    def trades(self):
        return self.api_request(self.url_base + 'Trades')
    
    def orderbook(self):
        return self.api_request(self.url_base + 'Orderbook')

