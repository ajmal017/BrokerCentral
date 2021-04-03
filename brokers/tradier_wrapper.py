import requests
import datetime

class Tradier:
    def __init__(self, token, sandbox=True, account=None):
        self.token = token
        self.url = "https://sandbox.tradier.com/v1/" if sandbox else "https://api.tradier.com/v1/"
        self.account = account

    def get_option_code(self, symbol, date, type, strike):
        '''
        Gets option code from option details
        Input: Symbol (String, ex: AAPL), Date (Datetime), Type (String, options: [call, put])
               String (Float, ex: 125.0)
        Returns: Option Code (String, ex: AAPL210312C00117000)
        '''
        strike = float(strike)
        date = date.strftime('%y%m%d')
        strike = str(float(strike)).split('.')
        type = 'C' if type == 'call' else 'P'
        dollar = strike[0]
        cents = strike[1]
        dollar_pad = '0' * (5-len(dollar))
        cent_pad = '0' * (3-len(cents))
        return symbol + date + type + dollar_pad + dollar + cents + cent_pad

    def get_option_quote(self, symbol, date, type, strike):
        '''
        Gets option quote from quote details
        Input: Symbol (String, ex: AAPL), Date (Datetime), Type (String, options: [call, put])
               String (Float, ex: 125.0)
        Returns: Quote Details (JSON)
        '''
        response = requests.get(self.url + 'markets/quotes',
            params={'symbols': self.get_option_code(symbol, date, type, strike)},
            headers={'Authorization': 'Bearer ' + str(self.token), 'Accept': 'application/json'}
        )
        json_response = response.json()
        return json_response

    def get_option_quote_from_code(self, code):
        '''
        Gets option quote from option code
        Input: Option Code (String, ex: AAPL210312C00117000),
        Returns: Quote Details (JSON)
        '''
        response = requests.get(self.url + 'markets/quotes',
            params={'symbols': code},
            headers={'Authorization': 'Bearer ' + str(self.token), 'Accept': 'application/json'}
        )
        json_response = response.json()
        return json_response

    def place_option_order(self, symbol, code, quantity, side, type, duration, price=0, stop=0):
        '''
        Places an option order given details
        Input: Symbol (String, ex: AAPL), Option Code (String, ex: AAPL210312C00117000),
               Quantity (Integer, ex: 10),
               Side (String, options: [buy_to_open, buy_to_close, sell_to_open, sell_to_close]),
               Type (String, options: [market, limit, stop, stop_limit]),
               Duration (String, options: [day, gtc, pre, post]),
               Price (Float, Optional, only for limit and stop_limit orders),
               Stop (Float, Optional, only for stop and stop_limit orders)
        Returns: Order Details (JSON)
        '''
        response = requests.post(self.url + 'accounts/' + str(self.account) + '/orders',
            data={'class': 'option', 'symbol': symbol, 'option_symbol': code, 'side': side, 'quantity': str(quantity), 'type': type, 'duration': duration, 'price': format(price, '.2f'), 'stop': format(stop, '.2f')},
            headers={'Authorization': 'Bearer ' + str(self.token), 'Accept': 'application/json'}
            )
        json_response = response.json()
        return json_response

    def get_order(self, id):
        '''
        Gets details of placed order
        Input: Order ID (Integer, ex: 123456)
        Returns: Order Details (JSON)
        '''
        response = requests.get(self.url + 'accounts/' + str(self.account) + '/orders/' + str(id),
            params={'includeTags': 'false'},
            headers={'Authorization': 'Bearer ' + str(self.token), 'Accept': 'application/json'}
            )
        json_response = response.json()
        return json_response

    def get_account_positions(self):
        '''
        Gets account's positions
        Input: None
        Returns: Positions (JSON)
        '''
        response = requests.get(self.url + 'accounts/' + str(self.account) + '/positions',
            params={},
            headers={'Authorization': 'Bearer ' + str(self.token), 'Accept': 'application/json'}
            )
        json_response = response.json()
        return json_response
