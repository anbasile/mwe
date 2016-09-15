from flask import render_template, flash, redirect
from app import app
import os
import random
import json

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
