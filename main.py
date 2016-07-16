import csv
from algorithims.Baseline import Baseline

def main():
    text = raw_input("Enter text to grade: ")
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Baseline}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print Baseline.grade(text)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

def test():
    scores = [ [0,0] ]
    algos = [Baseline()]
    count = 0
    with open('data/testData.csv', 'rU') as corpus:
        rows = csv.reader(corpus)
        for row in rows:
            a = 0
            for algo in algos:
                hyp = algo.test(row[1])
                if hyp == int(row[0]):
                    scores[a][0] += 1
                else:
                    scores[a][1] += 1
                a += 1
            count += 1
    print "Baseline score: " + str(scores[0][0]) + " correct and " + str(scores[0][1]) + " incorrect. Total percentage: %.2f" % (float(float(scores[0][0])/(scores[0][0] + scores[0][1]))*100) + "% correct!"

if __name__ == '__main__':
    test()