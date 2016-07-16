import csv
class Baseline:
    
    cache = {}

    def formatThing(self, arr, name):
        if(len(arr) == 0):
            return name + ": []"
        else:
            string = arr[0][0] + "("+arr[0][1]+","+arr[0][2]+")"
            for i, item in enumerate(arr):
                if i == 0:
                    continue
                string += "," + arr[i][0] + "("+arr[i][1]+","+arr[i][2]+")"
            return name + ": [" + string + "]"

    def grade(self, text):
        words = [word.lower() for word in text.split(" ")]
        corpus = open("data/SentiWordNet_reformatted.csv")
        rows = csv.reader(corpus)
        pos = []
        neg = []
        neu = []
        score = [0,0]
        for row in rows:
            if row[0].lower() in words:
                if float(row[1]) == float(row[2]):
                    neu.append(row)
                elif float(row[1]) > float(row[2]):
                    pos.append(row)
                else:
                    neg.append(row)
                score[0] += float(row[1])
                score[1] += float(row[2])

        print formatThing(pos, "positive")
        print formatThing(neg, "negative")
        print formatThing(neu, "neutral")
        print "Final Score: [" + str(score[0]) + " vs. " + str(score[1]) + "]"
            
        if score[0] > score[1]:
            print "Text is Positive!"
        elif score[0] < score[1]:
            print "Text is Negative..."
        else:
            print "Text is Neutral."

    def test(self, text):
        words = [word.lower() for word in text.split(" ")]
        corpus = open("data/SentiWordNet_reformatted.csv")
        rows = csv.reader(corpus)
        
        if len(self.cache) != 147305:
            print "writing cache!"
            self.cache = {}
            for row in rows:
                self.cache[row[0].lower()] = [float(row[1]), float(row[2])]
                
        score = [0,0]
        for word in words:
            grade = self.cache.get(word, [0,0])
            score[0] += grade[0]
            score[1] += grade[1]
            
        if score[0] > score[1]:
            return 0
        elif score[0] < score[1]:
            return 1
        else:
            return 2