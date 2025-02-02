import sys, os
import requests
import base64
import json
from kivy.storage.jsonstore import JsonStore

BASE_PATH = os.path.abspath(__file__+ '/../../')

sys.path.append(BASE_PATH)
from inc.environment import Environment
from inc.consts.consts import Consts

class Storage:

    @staticmethod
    def logoff():
        resp = False
        try:
            storage = JsonStore(Consts.JSON_PATH)
            storage.delete('login')
            resp = True
        except:
            resp = False
        return resp
    
    @staticmethod
    def r_authtoken():
        resp = False
        try:
            storage = JsonStore(Consts.JSON_PATH)
            resp = storage['login']
            if resp['authToken']:
                resp = resp['authToken']
            else:
                resp = False
        except:
            resp = False
        return resp

# resp = Storage.r_authtoken()
# print(resp)