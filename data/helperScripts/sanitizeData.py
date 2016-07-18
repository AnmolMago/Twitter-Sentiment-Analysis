import csv, re

posC = csv.reader(open('data/raw/corpuses/poscorpus_raw.csv', 'rU'))
negC = csv.reader(open('data/raw/corpuses/negcorpus_raw.csv', 'rU'))
qusC = csv.reader(open('data/raw/corpuses/quscorpus_raw.csv', 'rU'))

def softClean():
    for corpus in [posC, negC, qusC]:
        data = {}
        for row in corpus:
            text = row[1].replace('\u2019', "'")\
                        .replace('\u2026', '...')\
                        .replace('\u201c', '"')\
                        .replace('\u201d', '"')\
                        .replace('\u2026', '...')\
                        .replace('\u2026', '...')
            data.append([ row[0], text])