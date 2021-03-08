import requests
import datetime

class Tradier:
    def __init__(self, token):
        self.token = token
        self.url = "https://sandbox.tradier.com/v1/"

    def get_option_code(self, symbol, date, type, strike):
        strike = float(strike)
        date = date.strftime('%y%m%d')
        strike = str(strike).split('.')
        type = 'C' if type == 'call' else 'P'
        dollar = strike[0]
        cents = strike[1]
        dollar_pad = '0' * (5-len(dollar))
        cent_pad = '0' * (3-len(cents))
        return symbol + date + type + dollar_pad + dollar + cents + cent_pad

    def get_option_quote(self, symbol, date, type, strike):
        response = requests.get(self.url + 'markets/quotes',
            params={'symbols': self.get_option_code(symbol, date, type, strike)},
            headers={'Authorization': 'Bearer ' + str(self.token), 'Accept': 'application/json'}
        )
        json_response = response.json()
        return json_response

    def get_option_quote_from_code(self, code):
        response = requests.get(self.url + 'markets/quotes',
            params={'symbols': code},
            headers={'Authorization': 'Bearer ' + str(self.token), 'Accept': 'application/json'}
        )
        json_response = response.json()
        return json_response
