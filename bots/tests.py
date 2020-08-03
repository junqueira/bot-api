# from app import app
import os, json
import unittest
from Bot import Bot
import requests
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()

class AppTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.bot = Bot()

    def test_get_bots(self):
        r = requests.get("http://localhost:8080/bots")
        if r.status_code == 200:
            return r.json()
        return None

    def test_registre_bot(self):
        _json = {"id":"36b9f842-ee97-11e8-9443-0242ac120002", 
        "name":"Aureo",
        'status': '200', 
        'return': 'success'}
        resp = self.bot.registreBot(_json)
        assert _json == resp

    def test_get_bot(self):
        _json = {"id": "36b9f842-ee97-11e8-9443-0242ac120002", 
        "name": "Aureo", 
        "return": "success", 
        "status": "200"}
        resp = self.bot.getBot(_json.get("id"))
        resp = eval(json.dumps(resp))
        _json['time'] = resp['time']
        assert _json == resp

    def test_registre_message(self):
        _json = {"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
            "timestamp": "2018-11-16T23:30:52.6917722Z",
            "from": "36b9f842-ee97-11e8-9443-0242ac120002",
            "to": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
            "text": "Oi! Como posso te ajudar?",
            "status": "200", "return": "success"}
        resp = self.bot.registreMessage(_json)
        _json['time'] = resp['time']
        assert _json == resp

    def test_get_messages(self):
        _json = {"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1", 
            "from": "36b9f842-ee97-11e8-9443-0242ac120002", 
            "return": "success", 
            "status": "200", 
            "text": "Oi! Como posso te ajudar?", 
            "timestamp": "2018-11-16T23:30:52.6917722Z",
            "to": "16edd3b3-3f75-40df-af07-2a3813a79ce9"}
        resp = self.bot.getMessages(_json.get("to"))
        _json['time'] = resp['time']
        assert _json == resp

    def test_get_messages_conversation(self):
        _json = {"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1", 
            "from": "36b9f842-ee97-11e8-9443-0242ac120002", 
            "return": "success", "status": "200", 
            "text": "Oi! Como posso te ajudar?", 
            "timestamp": "2018-11-16T23:30:52.6917722Z", 
            "to": "16edd3b3-3f75-40df-af07-2a3813a79ce9"}
        resp = self.bot.getMessagesConversation(_json.get("conversationId"))
        resp = eval(json.dumps(resp))
        _json['time'] = resp.get('16edd3b3-3f75-40df-af07-2a3813a79ce9')['time']
        assert _json in resp.values()

if __name__ == '__main__':
    unittest.main()