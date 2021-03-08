from brokers.tda_wrapper import TDAWrapper
from brokers.etrade_wrapper import ETradeWrapper
from brokers.tradier_wrapper import Tradier

import json
import os.path
import sys
import datetime
 # testing

def read_config():
    with open("config.json", "r") as jsonfile:
        data = json.load(jsonfile)
    return data

def test_tda(data):
    tda = TDAWrapper(data['tda']['token_path'], data['tda']['api_key'], data['tda']['redirect_uri'])
    tda_client = tda.c
    ids = tda.get_account_ids()
    #tda.get_account_positions(ids[1])

def test_etrade(data):
    etrade = ETradeWrapper(data['etrade']['consumer_key'], data['etrade']['consumer_secret'], data['etrade']['tokens'])
    etrade.get_accounts()

def main():
    if os.path.isfile('config.json'):
        data = read_config()
    else:
        print('Run python setup.py first.')
        sys.exit(1)
    #test_etrade(data)
    #test_tda(data)
    tradier = Tradier(data['tradier']['token'])
    date = datetime.date(2021, 3, 19)
    tradier.get_option_quote('AAPL', date, 'call', 122)

if __name__ == "__main__":
    main()
