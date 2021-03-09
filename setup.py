from brokers.tda_wrapper import TDAWrapper
from brokers.etrade_wrapper import ETradeWrapper
import json
import os

print('Setup BrokerCentral')
print()
print("Choose which broker to setup: ")
print('--------------------------------')
print('1. TD Ameritrade')
print('2. E*Trade')
print('3. Tradier Market API')
print('4. Tradier Sandbox Trading')
print('5. All')
print()
choice = int(input('Your Choice: '))
config, tda_dict, e_dict, tradier_token, sand_dict = {}, {}, {}, {}, {}

def dump():
    config = {}
    config['tda'] = tda_dict
    config['etrade'] = e_dict
    config['tradier'] = {}
    config['tradier']['token'] = tradier_token
    config['tradier']['sandbox'] = sand_dict

    myJSON = json.dumps(config)

    with open("config.json", "w") as jsonfile:
        jsonfile.write(myJSON)

if os.path.isfile('config.json') == False:
    dump()

if choice != 5:
    with open("config.json", "r") as jsonfile:
        config = json.load(jsonfile)
    tda_dict, e_dict, tradier_token, sand_dict = config['tda'], config['etrade'], config['tradier']['token'], config['tradier']['sandbox']


if choice == 5 or choice == 1:
    print('Setup TD Ameritrade API')
    token_path = input('Enter your desired token path (brokercentral/path/to/token.pickle): ')
    api_key = input('Enter your API Key (CONSUMERID@AMER.OAUTHAPP): ')
    redirect_uri = input('Enter the redirect uri: ')
    tda = TDAWrapper(token_path, api_key, redirect_uri)
    tda_dict = {
        'token_path': token_path,
        'api_key': api_key,
        'redirect_uri': redirect_uri
    }
    print()
if choice == 5 or choice == 2:
    print('Setup E*Trade API')
    consumer_key = input('Enter your consumer key: ')
    consumer_secret = input('Enter your consumer secret: ')
    etrade = ETradeWrapper(consumer_key, consumer_secret, setup=True)
    tokens = etrade.get_tokens()
    e_dict = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'tokens': tokens
    }
    print()
if choice == 5 or choice == 3:
    print('Setup Tradier API')
    tradier_token = input("Enter your app's token: ")
    print()
if choice == 5 or choice == 4:
    print('Setup Tradier Papertrading')
    acc = input('Enter sanbox account number: ')
    sanbox_token = input('Enter sandbox account token: ')
    sand_dict = {
        'account': acc,
        'token': sanbox_token
    }

dump()
print("Saved!")
