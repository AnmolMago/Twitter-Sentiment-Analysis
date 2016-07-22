import csv, nltk, time
from data.helperScripts.sanitizeData import clean

posC = csv.reader(open('data/clean/poscorpus.csv', 'rU'))
negC = csv.reader(open('data/clean/negcorpus.csv', 'rU'))
qusC = csv.reader(open('data/clean/quscorpus.csv', 'rU'))

class NLTK():
    vocab = []
    trainingTweets = []
    NBClassifier = None

    def __init__(self):
        start_time = time.time()
        for corpus in[posC, negC, qusC]:
            count = 0
            for row in corpus:
                row[0] = row[0].lower()
                row[1] = clean(row[1].lower())
                self.trainingTweets.append( (self.getFeatureVector(row[1]), row[0]) )
                count += 1
        training_set = nltk.classify.util.apply_features(self.extract_features_complete, self.trainingTweets)
        self.NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
        print "NLTK Naive Bayes initialization and training time: " + str(time.time() - start_time)

    def test(self, tweet):
        return self.NBClassifier.classify(self.extract_features_complete(self.getFeatureVector(tweet)))

    def getFeatureVector(self, tweet):
        featureVector = []
        tweet = clean(tweet)
        words = tweet.split(" ")
        for w in words:
            featureVector.append(w.lower())
            if w.lower() not in self.vocab:
                self.vocab.append(w.lower())
        return featureVector

    def extract_features_complete(self, tweet):
        tweet_words = set(tweet)
        features = {}
        for word in self.vocab:
            features['contains(%s)' % word] = (word in tweet_words)
        return features
    
    def __exit__(self, exc_type, exc_value, traceback):
        print "EXIT CALLLEDDDD"
        print NBClassifier.show_most_informative_features(10)