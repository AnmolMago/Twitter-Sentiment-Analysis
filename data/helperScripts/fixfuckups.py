import csv
posC = csv.reader(open('data/clean/poscorpus.csv', 'rU'))
negC = csv.reader(open('data/clean/negcorpus.csv', 'rU'))
qusC = csv.reader(open('data/clean/quscorpus.csv', 'rU'))

def toomanycells():
    actC = csv.reader(open('data/raw/corpuses/activecorpus_raw.csv', 'rU'))
    count = 0
    data = []
    for row in actC:
        if len(row) > 2:
            text = ""
            for i, val in enumerate(row):
                if i != 0:
                    text = text + row[i]
            data.append([row[0], text])
            count += 1
        elif not "E+17" in row[1]:
            data.append([row[0], row[1]])
    wr = csv.writer(open('data/raw/corpuses/activecorpus_raw.csv', 'wb'))
    wr.writerows(data)
    print count

def lookOverQuestions():
    testD = csv.reader(open('data/testData.csv', 'rU'))
    data = []
    count = 0
    for row in testD:
        if row[0] == "3" and not "?" in row[1]:
            print row[1]
            count += 1
    #         cmd = raw_input("??: ")
    #         if cmd == "1":
    #             data.append([9, row[1]])
    #         else:
    #             data.append([row[0], row[1]])
    #     else:
    #         data.append([row[0], row[1]])
    # wr = csv.writer(open('data/testData.csv', 'wb'))
    # wr.writerows(data)
    print count

def find7525line():
    total = [5386.0,5243.0,5295.0]
    corpusC = 0
    for corpus in[posC, negC, qusC]:
        # total = 0.0
        # for row in corpus:
        #     total += 1.0
        # print total
        cur = 0.0
        for row in corpus:
            cur += 1.0
            if cur / total[corpusC] > 0.75:
                print row[1]
                break
        corpusC += 1

if __name__ == "__main__":
    find7525line()