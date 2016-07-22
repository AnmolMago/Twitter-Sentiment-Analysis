import csv, time
from algorithims.Baseline import Baseline
from algorithims.NaiveBayes import NaiveBayes
from algorithims.NLTK import NLTK
from data.helperScripts.sanitizeData import clean

def main():
    text = raw_input("Enter text to grade: ")
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Baseline}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print Baseline.grade(text)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~{Naive Bayes}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print NLTK().grade(text)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

def test():
    scores = {"Baseline":[0,0], "NLTK":[0,0], "NaiveBayes":[0,0]}
    testingTime = {"Baseline":0.0, "NLTK":0.0, "NaiveBayes":0.0}
    algos = {"Baseline":Baseline(), "NLTK":NLTK(), "NaiveBayes":NaiveBayes()}
    count = 0
    with open('data/testData.csv', 'rU') as corpus:
        rows = csv.reader(corpus)
        for row in rows:
            for name, algo in algos.items():
                if row[0] == "2":
                    continue
                count += 1
                start_time = time.time()
                hyp = algo.test(clean(row[1]))
                testingTime[name] += time.time() - start_time
                if hyp == row[0]:
                    scores[name][0] += 1
                else:
                    # print clean(row[1])
                    # print hyp + " vs. " + row[0]
                    scores[name][1] += 1
    print "\n\n"
    for name, scs in scores.items():
        print name + " score " + str(scs[0]) + " correct and " + str(scs[1]) + " incorrect. Total percentage: %.2f" % (float(float(scs[0])/(scs[0] + scs[1]))*100) + "% correct!"
    print "\n\n"
    for name, scores in scores.items():
        print "Testing time statistics for "+name+": {Total: " + str(testingTime[name]) + ", Average: " + str(testingTime[name]/count) + "}"

if __name__ == '__main__':
    test()