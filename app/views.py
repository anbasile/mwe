from flask import render_template, flash, redirect
from app import app
from .forms import tryForm
import pandas as pd
import numpy as np
from .words import calculate

dataset = [
    ['corso','fuoco','entrare','mondiale','interessi'],
    ['fa','canzone','unico','fronte','messaggio'],
    ['privata','piatto','sete','gridare','perdono'],
    ['meccanico','muro','torre','catena','corona'],
    ['pane','a terra','piuma','guanti','elastico' ],
    ['scuola','computer','clinica','tasse','tombola'],
    ['dolce','capitano','gesu','animale','bella'],
    ['andare','morte','sogno','moglie','case'],
    ['esempio','dottore','senza','conservare','pieno'],
    ['oro','mare','parte','bocca','sergio'],
    ['lettera','fiducia','agnelli','difensore','parcella'],
    ['morbida','rossa','trucco','labbra','disegno'],
    ['giornale','bianco','proverbi','fiera','divorare'],
    ['rosso','elettore','uccello','virtu','punto'],
    ['aprire','fondo','messaggio','varo','latte'],
    ['volare','corso','anni','ghiaccio','romanzo' ],
    ['nazionale','onore','guida','vana','bastardi'],
    ['lingua','occhio','pasta','levare','radice'],
    ['conoscenza','leggere','fedele','bella','omaggio'],
    ['vittoria','buco','pane','lacrime','toppa'],
    ['sotto','campo','mestiere','asino','pazzo'],
    ['russa','scacchi','nascere','notte','aglio'],
    ['carta','persona','forza','prova','attività' ],
    ['buoi','dito','botte','donna','mirella'],
    ['voce','regina','nave','volpe','rosso'],
#    ['punto','carabienieri','rosso','nuova','gas'],
    ['metro','ragazza','facce','elevare','letto'],
    ['pari','pace','sosta','motivo','famiglia'],
    ['secondo','porto','allievo','linea','pesce'],
    ['maggio','giardino','valle','nudo','sole'],
    ['uomo','gioco','morso','acqua','messi']
]

@app.route('/', methods=('GET', 'POST'))

@app.route('/index', methods=('GET', 'POST'))
def index():
    words = dataset[np.random.randint(0,len(dataset))]
    form = tryForm()
    machineguess = 0
    if form.validate_on_submit():
        return render_template('results.html',
                               form=form,
                               machineguess= calculate(words)[0],
                               url = calculate(words)[1]
                               )
                               
    return render_template('index.html',
                           form=form,
                           words=words
                           )
