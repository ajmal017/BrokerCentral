from brokers.tda_wrapper import TDAWrapper
import json

token_path = input('Enter your token path (/path/to/token.pickle): ')
api_key = input('Enter your API Key (CONSUMERID@AMER.OAUTHAPP): ')
redirect_uri = input('Enter the redirect uri: ')

config = {
    'token_path': token_path,
    'api_key': api_key,
    'redirect_uri': redirect_uri
}

myJSON = json.dumps(config)

with open("config.json", "w") as jsonfile:
    jsonfile.write(myJSON)
    print("Saved!")

TDAWrapper(token_path, api_key, redirect_uri)
