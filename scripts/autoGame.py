import csv 
import json

#pos:
# n: noun
# v: verb
# j: adj
# r: adv
# a: art
# p: pron
# i: prep
# c: coord
# d: determiner
# e: existential
# m: numbers
# t: to
# u: interjection
# x: not
# z: single/plural letters

COLLOCATES_POS_CONSTRAINTS = {
    'n': {max: 2},
    'v': {max: 2},
    'j': {max: 2},
    'i': {max: 1}
}

GAME_DICT = {}

# this is the tsv file from the data in http://www.collocates.info/entriesWithCollocates.txt
with open('entriesSamplesWithCollocates.tsv','r') as tsv:
    tsvin = csv.reader(tsv, delimiter='\t')
    entry_key = None
    entry_value = []
    pos_value = []
    for fields in tsvin:
        key, pos_key, col, pos_col = fields[1:5]
        if pos_key!='n':
            continue
        if key==entry_key:
            if len(entry_value)==5:
                continue
        else:
            entry_key = key
            entry_value = []
            pos_value = []
            GAME_DICT[entry_key] = entry_value
        if pos_col not in COLLOCATES_POS_CONSTRAINTS.keys() or \
           pos_value.count(pos_col)>COLLOCATES_POS_CONSTRAINTS[pos_col]:
            continue
        entry_value.append(col)
        pos_value.append(pos_col)

GAME_DICT = { k:v for k, v in GAME_DICT.items() if len(v)==5 }

with open('autoGame.json', 'w') as fp:
    json.dump(GAME_DICT, fp, indent=4)

print len(GAME_DICT)