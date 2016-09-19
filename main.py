import csv, time
from algorithims.Baseline import Baseline
from algorithims.NaiveBayes import NaiveBayes
from algorithims.NLTK import NLTK
from data.helperScripts.sanitizeData import clean

def main():
    text = raw_input("Enter text to grade: ")
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Baseline}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" 
    print Baseline().grade(text)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~{Naive Bayes}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print NaiveBayes().grade(text)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

def test():
    # "Baseline":[0.0,0.0], "NLTK":[0.0,0.0], 
    scores = {}
    percision = {}
    recall = {}
    testingTime = {}
    algos = {"Baseline":Baseline(), "NLTK":NLTK(), "NaiveBayes":NaiveBayes()}
    count = 0
    with open('data/testData.csv', 'rU') as corpus:
        rows = csv.reader(corpus)
        for row in rows:
            for name, algo in algos.items():
                if not name in scores:
                    scores[name] = [0.0,0.0]
                    percision[name] = {}
                    recall[name] = {}
                    testingTime[name] = 0.0
                    for senti in ["positive", "negative", "question"]:
                        percision[name][senti] = [0.0,0.0]
                        recall[name][senti] = [0.0,0.0]
                count += 1
                start_time = time.time()
                hyp = algo.test(clean(row[1]))
                testingTime[name] += time.time() - start_time
                if hyp == row[0]:
                    scores[name][0] += 1
                    scores[name][1] += 1
                    percision[name][hyp][0] += 1
                    percision[name][hyp][1] += 1
                    recall[name][hyp][0] += 1
                    recall[name][hyp][1] += 1
                else:
                    # print clean(row[1])
                    # print hyp + " vs. " + row[0]
                    scores[name][1] += 1
                    for senti in ["positive", "negative", "question"]:
                        if hyp == senti and row[0] != senti:
                            percision[name][senti][1] += 1
                        if hyp != senti and row[0] == senti:
                            recall[name][senti][1] += 1

    print "\n\n"
    for name, scs in scores.items():
        print name + " score " + str(scs[0]) + " correct and " + str(scs[1]) + " incorrect. Total percentage:", scs[0]/scs[1]*100, "% correct!"
    print "\n\n"
    for name, scs in scores.items():
        print "For", name
        for senti in ["positive", "negative", "question"]:
            print "sentiment", senti + ":", "percision", percision[name][senti][0]/percision[name][senti][1]*100, "% and recall", recall[name][senti][0]/recall[name][senti][1]*100,"%"
    print "\n\n"
    for name, scs in scores.items():
        print "Testing time statistics for "+name+": {Total: " + str(testingTime[name]) + ", Average: " + str(testingTime[name]/count) + "}"

if __name__ == '__main__':
    main()