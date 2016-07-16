import os, csv, random

data = []

def main():
    temp = open('tempcorpus.csv', 'r')
    corpus = open('activecorpus.csv', 'ab')
    tweets = csv.reader(temp)
    for tweet in tweets:
        print tweet[0] + ": " + tweet[1].encode('unicode_escape').decode('utf-8')
        if int(tweet[0]) > 753613937535545345:
            continue
        if len(tweet[1]) > 50 and random.random() < 0.3333:
            text = tweet[1].replace(":))", "").replace(":)", "").replace(":P", "").replace(":-)", "").replace(": )", "").replace(":D", "").replace("=)", "").replace(":(", "").replace(":-(", "").replace(": (", "")
            data.append(['positive', text.encode('unicode_escape').decode('utf-8') + "\n"])
        else:
            data.append(['positive', tweet[1].encode('unicode_escape').decode('utf-8') + "\n"])

    wr = csv.writer(corpus, delimiter=',')
    wr.writerows(data)
    corpus.close()
    temp.close()
    print "DONE"

if __name__ == '__main__':
    main()