import csv

posC = csv.reader(open('data/raw/corpuses/poscorpus_raw.csv', 'rU'))
negC = csv.reader(open('data/raw/corpuses/negcorpus_raw.csv', 'rU'))
qusC = csv.reader(open('data/raw/corpuses/quscorpus_raw.csv', 'rU'))
actC = csv.reader(open('data/raw/corpuses/activecorpus_raw.csv', 'rU'))
senC = csv.reader(open('data/testData/sentiment140/testdata.manual.2009.06.14.csv', 'rU'))

data = {}

for corpus in [posC, negC, qusC]:
    for row in corpus:
        if row[1].endswith("E+17"):
            continue
        if row[0] == "positive":
            data[row[1].lower()] = [0, row[1]]
        elif row[0] == "negative":
            data[row[1].lower()] = [1, row[1]]
        elif row[0] == "neutral":
            data[row[1].lower()] = [2, row[1]]
        elif row[0] == "question":
            data[row[1].lower()] = [3, row[1]]

wr = csv.writer(open('data/corpus.csv', 'wb'), delimiter=',')
wr.writerows(data.values())
data = {}
duplicate = 0
count = 0
for row in actC:
    count += 1
    if row[1].endswith("E+17"):
        continue
    if row[0] == "positive":
        data[row[1].lower()] = [0, row[1]]
    elif row[0] == "negative":
        data[row[1].lower()] = [1, row[1]]
    elif row[0] == "neutral":
        data[row[1].lower()] = [2, row[1]]
    elif row[0] == "question":
        data[row[1].lower()] = [3, row[1]]

print len(data)
print duplicate
print count
for row in senC:
    if row[5].endswith("E+17"):
        continue
    if row[0] == "4":
        data[row[5].lower()] = [0, row[5]]
    elif row[0] == "0":
        data[row[5].lower()] = [1, row[5]]
    elif row[0] == "2":
        data[row[5].lower()] = [2, row[5]]
    else:
        print "Weird thing found: " + row[0]
print len(data)

wr = csv.writer(open('data/testData.csv', 'wb'), delimiter=',')
wr.writerows(data.values())
