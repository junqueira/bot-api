# -*- coding: utf-8 -*-
from flask import Flask, request, session, redirect, url_for, escape, Response
from flask_restful import reqparse, abort, Api, Resource
from Bot import Bot
import os, time, json

app = Flask(__name__)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'
bot = None

#bots
@app.route('/bots/add', methods=['POST'])
def addBot():
    ret = bot.registreBot(eval(request.data))
    return json.dumps(ret)

@app.route('/bots/<id>', methods=['GET'])
def getBot(id):
    ret = bot.getBot(id)
    return json.dumps(ret)

#message
@app.route('/messages/add', methods=['POST'])
def addMessage():
    ret = bot.registreMessage(eval(request.data))
    return json.dumps(ret)

@app.route('/messages/<id>', methods=['GET'])
def getMessages(id):
    ret = bot.getMessages(id)
    return json.dumps(ret)

@app.route('/messages/conversationId=<conversationId>', methods=['GET'])
def getMessagesConversation(conversationId):
    ret = bot.getMessagesConversation(conversationId)
    return json.dumps(ret)

def initBot():
    global bot
    bot = Bot()

if __name__ == '__main__':
    initBot()
    # sudo lsof -t -i tcp:8080 | xargs kill
    app.run(debug=False, host='0.0.0.0', port=8081)
