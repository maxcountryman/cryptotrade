import urllib
import json
import socket

from urlparse import urljoin

import public_api

socket.setdefaulttimeout(15) # 15 seconds


class Trader(object):
    '''Super class for trading platforms such as MtGox and TradeHill. 
    
    Inherit this class to define new platforms.
    '''
    
    def api_request(self, url, url_parameters=None, request_type='POST'):
        '''Processes an API request using specified URL parameters, 
        `url_parameters`. A URL is built by using `url_path` and concatenating 
        it with `url_parameters.` In the future, `request_type` may be used to 
        change the HTTP request method; for now the default is set to POST as 
        the two major trading platforms use POST requests.
        
        Returns JSON response.
        '''
        
        if url_parameters:
            parameters = urllib.urlencode(url_parameters.update(self.auth))
            url = url + '?' + parameters
        
        try:
            response = urllib.urlopen(url, request_type).read()
            response = json.loads(response)
        except Exception, e:
            return e
        
        return response


class MtGox(Trader, public_api.MtGoxPublic):
    '''MtGox trading API wrapper; mtgox.com.'''
    
    def __init__(self, username=None, password=None):
        self.url_base = 'https://mtgox.com/code/'
        self.auth = {
            'name': username, 
            'pass': password
            }
    
    def balance(self):
        '''Our current balance. Takes no parameters.
        
        Returns balance.
        '''
        
        return self.api_request(self.url_base + 'getFunds.php')
        
    def buy(self, amount, price):
        '''Places an order to buy BTC. Here `price` indicates limit price and 
        `amount` indicates desired number of BTC to purchase.
        
        Returns list of open orders.
        '''
        
        parameters = {'amount': amount, 'price': price}
        return self.api_request(self.url_base + 'buyBTC.php', parameters)
        
    def sell(self, amount, price):
        '''Places an order to sell BTC. Here `price` indicates limit price and
        `amount` indicates desired number of BTC to sell.
        
        Return list of open orders.
        '''
        
        parameters = {'amount': amount, 'price': price}
        return self.api_request(self.url_base + 'sellBTC.php', parameters)
        
    def orders(self):
        '''Fetches a list of open orders. `oid` indicates the unique order ID.
        `type: 1` for sell order or `type: 2` for buy order. `status: 1` 
        indicates active and `status: 2` indicates not enough funds.
        
        Returns `oid`, `type`, and `status`.
        '''
        
        return self.api_request(self.url_base + 'getOrders.php')
    
    def cancel(self, order_id, order_type):
        '''Canels an active order. `order_id` indicates unique order ID and 
        `order_type`, either `order_type=1` or `order_type=2` indicates sell 
        order and buy order, respectively.
        
        Returns `oid` and `type`.
        '''
        
        parameters = {'oid': order_id, 'type': order_type}
        return self.api_request(self.url_base + 'cancelOrder.php', parameters)
    
    def send(self, amount, address):
        '''TODO'''
        
        parameters = {'amount': amount, 'btca': address, 'group1': 'BTC'}
        return self.api_request(self.url_base + 'withdraw.php', parameters)


class TradeHill(Trader, public_api.TradeHillPublic):
    '''TradeHill trading API wrapper; tradehill.com''' 
    
    def __init__(self, username=None, password=None, currency='USD'):
        self.api_version = 'APIv1'
        self.currencies = ['USD', 'AUD', 'CAD', 'CLP', 'EUR', 'INR', 'LR']
        if not currency in self.currencies:
            raise Exception('Currency value is invalid')
        self.currency = currency
        self.url_base = 'https://api.tradehill.com/'
        self.url_path = '/{0}/{1}/'.format(self.api_version, self.currency)
        self.url_base = urljoin(self.url_base, self.url_path)
        self.auth = {
                'name': username, 
                'pass': password
                }
    
    def balance(self):
        '''Our current balance for the specified currency, e.g. USD and for BTC.
        Takes no parameters.
        
        Returns a dictionary of Currency, Amount pairs.
        '''
        
        return self.api_request(self.url_base + 'GetBalance')
    
    def buy(self, price, amount):
        '''Submits a limit order to buy BTC using specificed currency, e.g. 
        USD. Limit order price is indicated by `price`. The desired amount to 
        purchase is indicated by `amount`.
        
        Returns a list of open orders.
        '''
        
        parameters = {'price': price, 'amount': amount}
        return self.api_request(self.url_base + 'BuyBTC', parameters)
        
    def sell(self, price, amount):
        '''Submits a limit order to sell BTC using specificed currency, e.g. 
        USD. Limit order price is indicated by `price`. The desired amount to 
        sell is indicated by `amount`.
        
        Returns a list of open orders.
        '''
        
        parameters = {'price': price, 'amount': amount}
        return self.api_request(self.url_base + 'SellBTC', parameters)
        
    def orders(self):
        '''Get the current open orders in given currency, e.g. USD.
                
        Returns a dictionary containing orders information.
        '''
        
        return self.api_request(self.url_base + 'GetOrders')
    
    def cancel(self, order_id):
        '''Submits a request to cancel an open order. Request will take time 
        to process, up to five seconds.
        
        Returns list of open orders.
        '''
        
        parameters = {'oid': order_id}
        
        return self.api_request(self.url_base + 'CancelOrder', parameters)
    
    # Not yet implemented by external API
    #def send(self):
    #    parameters = {}
    #    return self.api_request(self.url_base + 'Send', parameters)

