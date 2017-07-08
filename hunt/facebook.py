import requests
import json
import facebook


class FacebookHelper:

    APP_ID = str('1901884306696195')
    APP_SECRET = str('1dff38165883b52d86c87a332989df58')
    REDIRECT_URI = 'http://localhost/login/'
    CODE_URL = 'https://www.facebook.com/v2.8/dialog/oauth'
    GRAPH_API_URL = 'https://graph.facebook.com/v2.8/me'
    ACCESS_TOKEN_URL = 'https://graph.facebook.com/v2.8/oauth/access_token'
    ACCESS_TOKEN = None

    def __init__(self, code):
        token = requests.get(self.ACCESS_TOKEN_URL, params={'client_id': self.APP_ID, 'redirect_uri': self.REDIRECT_URI,
                                                        'client_secret': self.APP_SECRET, 'code': code}).json()
        print("ACCESS_TOKEN IS " + token['access_token'])
        self.ACCESS_TOKEN = token['access_token']

    def get_details(self):
        if self.ACCESS_TOKEN is not None:
            details = requests.get(self.GRAPH_API_URL, {'fields': 'id,name', 'access_token': self.ACCESS_TOKEN}).json()
            print(details)
            return details













