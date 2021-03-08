import pyetrade


class ETradeWrapper:
    def __init__(self, key, secret, tokens=None, setup=False):
        self.consumer_key = key
        self.consumer_secret = secret
        if setup:
            oauth = pyetrade.ETradeOAuth(self.consumer_key, self.consumer_secret)
            print('Copy and paste this URL and follow the directions:')
            print(oauth.get_request_token())
            verifier_code = input("Enter verification code: ")
            self.tokens = oauth.get_access_token(verifier_code)
        else:
            self.tokens = tokens

    def get_tokens(self):
        return self.tokens

    def get_accounts(self):
        accounts = pyetrade.ETradeAccounts(self.consumer_key, self.consumer_secret, self.tokens['oauth_token'], self.tokens['oauth_token_secret'])
        print(accounts.list_accounts()['AccountListResponse']['Accounts'])
