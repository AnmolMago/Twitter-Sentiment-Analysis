#SentiWordNet Reformat
import os, csv

def get_words(row):
    words_ids = row[4].split(" ")
    words = [w.split("#")[0] for w in words_ids]
    return words

def main():
    SWN = open('raw/SentiWordNet_3.0.0_20130122.txt', 'r')
    data = []
    for line in SWN:
        if not line.startswith("#"):
            row = line.split("\t")
            words = get_words(row)
            for word in words:
                data.append([word, row[2], row[3], 1 - (float(row[2]) + float(row[3]))])
    corpus = open('SentiWordNet_reformatted.csv', 'wb')
    wr = csv.writer(corpus, delimiter=',')
    wr.writerows(data)
    corpus.close()

if __name__ == "__main__":
    main()