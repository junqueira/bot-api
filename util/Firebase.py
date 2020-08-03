import pyrebase
import os
import time
import json


class Firebase(object):

    def __init__(self):
        config = {"apiKey": os.environ.get('API_KEY_FIREBASE'),
                  "authDomain": os.environ.get('AUTH_DOMAIN_FIREBASE'),
                  "databaseURL": os.environ.get('DATA_BASE_URL_FIREBASE'),
                  "storageBucket": os.environ.get('STORAGE_BUCKET_FIREBASE')
        }
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def registreBot(self, _json):
        _time = time.strftime("%Y-%m-%d %X")
        _json["time"] = _time
        _id = _json.get('id')
        ret = self.db.child("bots").child(_id).set(_json)
        ret["status"] = "200"
        ret["return"] = "success"
        ret["time"] = _time
        return ret

    def getBot(self, id):
        _bot = self.db.child("bots").child(id).get().val()
        return _bot

    def registreMessage(self, _json):
        _time = time.strftime("%Y-%m-%d %X")
        _json["time"] = _time
        _talk = _json.get('conversationId')
        _to = _json.get('to')
        ret = self.db.child("bots").child("messages") \
                     .child(_to).set(_json)
        ret = self.db.child("bots").child("conversation").child(_talk) \
                     .child(_to).set(_json)
        ret["status"] = "200"
        ret["return"] = "success"
        ret["time"] = _time
        return ret

    def getMessages(self, id):
        message = self.db.child("bots").child("messages") \
                      .child(id).get().val()
        return message

    def getMessagesConversation(self, conversationId):
        # import ipdb; ipdb.set_trace()
        msnConv = self.db.child("bots").child("conversation") \
                      .child(conversationId).get().val()
        return msnConv