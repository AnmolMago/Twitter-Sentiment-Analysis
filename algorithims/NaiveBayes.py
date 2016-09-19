import csv, json, math, time
from data.helperScripts.sanitizeData import clean

posC = csv.reader(open('data/clean/poscorpus.csv', 'rU'))
negC = csv.reader(open('data/clean/negcorpus.csv', 'rU'))
qusC = csv.reader(open('data/clean/quscorpus.csv', 'rU'))

class NaiveBayes(object):
    
    Bags = {}
    Vocab = {}
    CatSeen = {}

    def __init__(self):
        start_time = time.time()
        #load bags
        for corpus in[posC, negC, qusC]:
            for row in corpus:
                row[0] = row[0].lower()
                row[1] = clean(row[1].lower())

                if row[0] not in self.CatSeen:
                    self.CatSeen[row[0]] = 0.0
                self.CatSeen[row[0]] += 1.0

                if row[0] not in self.Bags:
                    self.Bags[row[0]] = {}

                for word, count in self.getWordCounts(row[1].split(" ")).items():
                    self.Bags[row[0]][word.lower()] = self.Bags[row[0]].get(word.lower(), 0.0) + count
                    if word.lower() not in self.Vocab:
                        self.Vocab[word.lower()] = 0.0
                    self.Vocab[word.lower()] += count
        # print "My Naive Bayes implementation's initialization and training time: " + str(time.time() - start_time)


    def getWordCounts(self, words):
        wc = {}
        for word in words:
            wc[word] = wc.get(word, 0.0) + 1.0
        return wc

    def test(self, text):
        TotalLogScores = {
            "positive":0.0,
            "negative":0.0,
            "question":0.0,
        }
        TotalCatSeen = sum(self.CatSeen.values())
        PriorLogCatScore = {
            "positive":math.log(self.CatSeen["positive"]/TotalCatSeen),
            "negative":math.log(self.CatSeen["negative"]/TotalCatSeen),
            "question":math.log(self.CatSeen["question"]/TotalCatSeen),
        }

        for word, count in self.getWordCounts(text.split(" ")).items():
            if not word in self.Vocab: #or word in stopwords list
                continue
            
            p_word = self.Vocab[word] / sum(self.Vocab.values())
            scores = {}
            for cat in TotalLogScores:
                scores[cat] = self.Bags[cat].get(word, 0.0)/sum(self.Bags[cat].values())
            
            for cat, score in scores.items():
                if score > 0:
                    TotalLogScores[cat] += math.log(count * score/p_word)

        Epsilon = 0

        TotalScores = {}
        for cat, logScore in TotalLogScores.items():
            TotalScores[cat] = math.exp(logScore)

        if TotalScores["question"] > ( TotalScores["positive"] + Epsilon ) and TotalScores["question"] > ( TotalScores["negative"] + Epsilon ):
            return "question"
        elif TotalScores["positive"] > ( TotalScores["negative"] + Epsilon ):# and TotalScores["positive"] > ( TotalScores["question"] + Epsilon ):
            return "positive"
        elif TotalScores["negative"] > ( TotalScores["positive"] + Epsilon ) and TotalScores["negative"] > ( TotalScores["question"] + Epsilon ):
            return "negative"
        else:
            return max(TotalScores, key=TotalScores.get)

    def grade(self, text):
        TotalLogScores = {
            "positive":0.0,
            "negative":0.0,
            "question":0.0,
        }
        TotalCatSeen = sum(self.CatSeen.values())
        PriorLogCatScore = {
            "positive":math.log(self.CatSeen["positive"]/TotalCatSeen),
            "negative":math.log(self.CatSeen["negative"]/TotalCatSeen),
            "question":math.log(self.CatSeen["question"]/TotalCatSeen),
        }

        for word, count in self.getWordCounts(text.split(" ")).items():
            if not word in self.Vocab: #or word in stopwords list
                continue
            
            p_word = self.Vocab[word] / sum(self.Vocab.values())
            scores = {}
            for cat in TotalLogScores:
                scores[cat] = self.Bags[cat].get(word, 0.0)/sum(self.Bags[cat].values())
            
            for cat, score in scores.items():
                if score > 0:
                    TotalLogScores[cat] += math.log(count * score/p_word)

        Epsilon = 0

        TotalScores = {}
        for cat, logScore in TotalLogScores.items():
            TotalScores[cat] = math.exp(logScore)

        if TotalScores["question"] > ( TotalScores["positive"] + Epsilon ) and TotalScores["question"] > ( TotalScores["negative"] + Epsilon ):
            return "Text is a Question..."
        elif TotalScores["positive"] > ( TotalScores["negative"] + Epsilon ):# and TotalScores["positive"] > ( TotalScores["question"] + Epsilon ):
            return "Text is positive"
        elif TotalScores["negative"] > ( TotalScores["positive"] + Epsilon ) and TotalScores["negative"] > ( TotalScores["question"] + Epsilon ):
            return "Text is negative"
        else:
            return "Text is neutral"

if __name__ == '__main__':
    n = NaiveBayes()