import csv, re

# {'positive': 5388}
# {'negative': 5251}
# {'question': 5295}
posC = csv.reader(open('data/raw/corpuses/poscorpus_raw.csv', 'rU'))
negC = csv.reader(open('data/raw/corpuses/negcorpus_raw.csv', 'rU'))
qusC = csv.reader(open('data/raw/corpuses/quscorpus_raw.csv', 'rU'))

words = {}

for corpus in [posC, negC, qusC]:
    for row in corpus:
        wordList = re.sub("[^\w]", " ",  row[1]).split()
        for word in wordList:
            words[word.lower()] = words.get(word.lower(), 0) + 1
    d_view = [ (v,k) for k,v in words.iteritems() ]
    d_view.sort(reverse=True)
    print d_view[:100]
    words = {}
    break