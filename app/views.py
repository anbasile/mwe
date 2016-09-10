from flask import render_template, flash, redirect
from app import app
import os
import random
import json

dataset = {
    'time': ['long','spend','short','give','working'],
    'way': ['long','go','get','come','easy'],
    'days': ['early','past','old','spent','take'],
    'parts': ['spare','component','constitutent','played','separate'],
    'case': ['court','present','particular','prosecution','adjourned'],
    'life': ['real','family','whole','public','saved'],
    'service': ['free','telephone','intelligence','security','regular'],
    'area': ['play','residential','wide','major','surrounding'],
    'course': ['training','main','first','take','start'],
    'hands': ['shook','wash','holding','raised','rubbed']
}

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
manual_url = os.path.join(SITE_ROOT, "static/data", "manual.json")
auto_url = os.path.join(SITE_ROOT, "static/data", "auto.json")
dataset = json.load(open(manual_url))
dataset2 = json.load(open(auto_url))

@app.route('/', methods=('GET', 'POST'))

@app.route('/index', methods=('GET', 'POST'))
def index():
    word = random.choice(list(dataset.keys()))
    words = dataset[word]
    return render_template('index.html',
                           solution=word,
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
