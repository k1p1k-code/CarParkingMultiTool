
import requests
from ..cptypes import Account, Noneheaders


def get_headers(idToken, json):
        return {
    'host' : 'us-central1-cp-multiplayer.cloudfunctions.net', 
    'authorization' : f'Bearer {idToken}', 
    'firebase-instance-id-token' : 'ePMUzsAGQb-f-NP9CQVsvJ:APA91bEI7czAgeEGx7qLl_U13REgY2bxindAuDiqGOYEwUtT7YZHwxGaz901AAoKAv8UborjjK7R78ldwkIJOqj9YmFrs6vz8eYqmBgp6VvGRvzxOZ01aAs',
    'content-type' : 'application/json; charset=utf-8',
    'content-length' : f'{len(str(json))}',
    'accept-encoding' : 'gzip',
    'user-agent' : 'okhttp/3.12.13'}





