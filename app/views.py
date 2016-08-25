from flask import render_template, flash, redirect
from app import app
from .forms import tryForm
import pandas as pd
import numpy as np
import random
from .words import calculate

dataset = {
    'time': ['long','spend','short','give','working'],
    'way': ['long','go','get','come','easy'],
    'days': ['early','past','old','spent','take'],
    'parts': ['spare','component','consitutent','played','separate'],
    'case': ['court','present','particular','prosecution','adjourned'],
    'life': ['real','family','whole','public','saved'],
    'service': ['free','telephone','intelligence','security','regular'],
    'area': ['play','residential','wide','major','surrounding'],
    'course': ['training','main','first','take','start'],
    'hands': ['shook','wash','holding','raised','rubbed']
}

@app.route('/', methods=('GET', 'POST'))

@app.route('/index', methods=('GET', 'POST'))
def index():
    words = random.choice(list(dataset.values()))

    return render_template('index.html',
                           words=words
                           )
