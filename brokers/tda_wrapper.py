# TD Ameritrade Hook

from tda import auth, client
import json

class TDAWrapper:
    def __init__(self, path, key, uri):
        self.token_path = path
        self.api_key = key
        self.redirect_uri = uri
        try:
            self.c = auth.client_from_token_file(self.token_path, self.api_key)
        except FileNotFoundError:
            from selenium import webdriver
            with webdriver.Chrome() as driver:
                self.c = auth.client_from_login_flow(driver, self.api_key, self.redirect_uri, self.token_path)

    def get_account_ids(self):
        ids = []
        for i in self.c.get_accounts().json():
            ids.append(i['securitiesAccount']['accountId'])
        return ids

    def get_account_balance(self, id):
        data = self.c.get_account(id).json()
        return data['securitiesAccount']['currentBalances']['liquidationValue']
