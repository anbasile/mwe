from flask import render_template, flash, redirect, request
from app import app
import os
import random
import json
import time
import requests

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
manual_url = os.path.join(SITE_ROOT, "static/data", "manual.json")
m_ex_url = os.path.join(SITE_ROOT, "static/data", "examples.json")
auto_url = os.path.join(SITE_ROOT, "static/data", "auto.json")

dataset = json.load(open(manual_url))
dataset2 = json.load(open(auto_url))
m_examples = json.load(open(m_ex_url))

@app.route('/', methods=('GET', 'POST'))

@app.route('/index', methods=('GET', 'POST'))
def index():
    word = random.choice(list(dataset.keys()))
    words = dataset[word]
    examples = m_examples[word]
    return render_template('index.html',
                           solution=word,
                           examples=examples,
                           words=words
                           )

@app.route('/auto-mode', methods=('GET', 'POST'))
def auto():
    word = random.choice(list(dataset2.keys()))
    words = dataset2[word]
    return render_template('index.html',
                           solution=word,
                           words=words
                           )

@app.route('/tg/webhook', methods=('POST'))
def telegram():
    BASEURL = 'https://api.telegram.org/bot271783166:AAGjjmD6Dj1T1r-urEr0o2JoKcQAZ1ZBCu4'
    sendUrl = BASEURL+'/sendMessage'
    content = request.get_json()
    text = content['message']['text']
    userid = content['message']['from']['id']
    word = random.choice(list(dataset.keys()))
    words = dataset[word]
    examples = m_examples[word]
    if text == '/play':
        # send set
        game = requests.post(sendUrl, data = {'chat_id':userid,'text': str(words)})
        time.sleep(60)
        # send solution
        solution = requests.post(sendUrl, data = {'chat_id':userid,'text': str(word)})
        time.sleep(1)
        # send examples
        ex = requests.post(sendUrl, data = {'chat_id':userid,'text': str(examples)})
        return "ok"
    return (requests.post(sendUrl, data = {'chat_id':userid,'text': "instructions"}))

