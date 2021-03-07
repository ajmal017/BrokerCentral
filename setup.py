from brokers.tda_wrapper import TDAWrapper
from brokers.etrade_wrapper import ETradeWrapper
import json

print('Setup TD Ameritrade API')

token_path = input('Enter your token path (/path/to/token.pickle): ')
api_key = input('Enter your API Key (CONSUMERID@AMER.OAUTHAPP): ')
redirect_uri = input('Enter the redirect uri: ')

print()

print('Setup E*Trade API')
consumer_key = input('Enter your consumer key: ')
consumer_secret = input('Enter your consumer secret: ')

tda = TDAWrapper(token_path, api_key, redirect_uri)
etrade = ETradeWrapper(consumer_key, consumer_secret, setup=True)
tokens = etrade.get_tokens()

config = {
    'tda': {
        'token_path': token_path,
        'api_key': api_key,
        'redirect_uri': redirect_uri
    },
    'etrade': {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'tokens': tokens
    }
}

myJSON = json.dumps(config)

with open("config.json", "w") as jsonfile:
    jsonfile.write(myJSON)
    print("Saved!")
