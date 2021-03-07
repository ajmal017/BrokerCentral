from brokers.tda_wrapper import TDAWrapper
import json
import os.path
import sys


def read_config():
    with open("config.json", "r") as jsonfile:
        data = json.load(jsonfile)
    return data

def main():
    if os.path.isfile('config.json'):
        data = read_config()
    else:
        print('Run python setup.py first.')
        sys.exit(1)
    tda = TDAWrapper(data['token_path'], data['api_key'], data['redirect_uri'])
    tda_client = tda.c
    ids = tda.get_account_ids()
    print(tda.get_account_balance(ids[1]))

if __name__ == "__main__":
    main()
