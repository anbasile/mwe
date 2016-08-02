import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd
import json
import networkx as nx
from networkx.readwrite import json_graph
import numpy as np
from lightning import Lightning
from colorsys import hsv_to_rgb
from sklearn import datasets
lgn = Lightning(host='http://public.lightning-viz.org')

def calculate(words):
    # instantiate a dictionary to later be filled with word:miscores
    wc = defaultdict(float)
    frames = []
    print("...it will take a while. Wait a sec...")
    for word in words:
        payload = {'searchstring': word.encode('ascii'),
                   'searchpositional':'word',
                   'searchpostag':'all',
                   'contextsize':'60c',
                   'sort2':'right',
                   'terminate':'100',
                   'searchtype':'coll',
                   'mistat':'on',
                   'collocspanleft':'2',
                   'collocspanright':'2',
                   'collocfilter':'noun'}

        r = requests.get("http://clic.cimec.unitn.it/cgi-bin/cqp/cqp.pl?corpuslist=WEBBIT", params=payload)
        soup = BeautifulSoup(r.content, 'lxml')

        # parse the html table and extract words and miscores. Add scores
    
        temp = []
        for tr in soup.find_all('tr')[1:]:
            tds = tr.find_all('td')
            word = tds[0].text.split('~~')[1]
            mi = float(tds[4].text)
            wc[word] += mi
            temp.append(map(lambda x:x.text,tds[0:]))
        x = pd.DataFrame(temp)
        df = pd.DataFrame()
        df['coll'] = x.ix[0:,0].apply(lambda x: x.split('~~')[1])
        df['word'] = x.ix[0:,0].apply(lambda x: x.split('~~')[0])
        df['mi'] = x.ix[0:,4]
        frames.append(df)

    #sort the results in decreasing order        
    results = []
    for w in sorted(wc, key=wc.get, reverse=True):
        results.append((w, wc[w]))

    #spit out the top result. If using ipython you can check the rest of the list by tiping `results`
    #viz part
    results_df = pd.concat(frames)

    G=nx.from_pandas_dataframe(results_df, 'word','coll',['mi'])
    mat = nx.adjacency_matrix(G).todense()
    viz = lgn.force(mat)
    vid = viz.id
    print(vid)
    url = '<iframe src="http://public.lightning-viz.org/visualizations/'+vid+'/iframe/" width=100% height=400px>'
    return (results[0][0].strip(),url)
