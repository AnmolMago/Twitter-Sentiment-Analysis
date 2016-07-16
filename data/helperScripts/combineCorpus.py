import csv

posC = csv.reader(open('data/raw/corpuses/poscorpus_raw.csv', 'rU'))
negC = csv.reader(open('data/raw/corpuses/negcorpus_raw.csv', 'rU'))
qusC = csv.reader(open('data/raw/corpuses/quscorpus_raw.csv', 'rU'))
actC = csv.reader(open('data/raw/corpuses/activecorpus_raw.csv', 'rU'))

data = []

for corpus in [posC, negC, qusC, actC]:
    for row in corpus:
        if row[1].endswith("E+17"):
            continue
        if row[0] == "positive":
            data.append([0, row[1]])
        elif row[0] == "negative":
            data.append([1, row[1]])
        elif row[0] == "neutral":
            data.append([2, row[1]])
        elif row[0] == "question":
            data.append([3, row[1]])

wr = csv.writer(open('data/corpus.csv', 'wb'), delimiter=',')
wr.writerows(data)