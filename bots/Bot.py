# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys, time, re, json
from math import sqrt
from datetime import datetime
from collections import defaultdict
sys.path.append(os.getcwd())
from util import Config, Logger, Firebase


class Bot(Logger):

    def __init__(self):
        Config.__init__(self)
        Logger.__init__(self)
        self.base = Firebase()
        self.env = self.conf.get("enviroment")
        
    def registreBot(self, _json):
        resp = self.base.registreBot(_json)
        return resp

    def getBot(self, id):
        resp = self.base.getBot(id)
        return resp

    def registreMessage(self, _json):
        resp = self.base.registreMessage(_json)
        return resp

    def getMessages(self, _json):
        resp = self.base.getMessages(_json)
        return resp
    
    def getMessagesConversation(self, _json):
        resp = self.base.getMessagesConversation(_json)
        return resp


