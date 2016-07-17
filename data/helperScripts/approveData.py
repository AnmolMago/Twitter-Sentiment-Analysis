import os, csv, random

data = []

def main():
    temp = open('data/testDataOld.csv', 'rU')
    corpus = open('data/testData.csv', 'ab')
    tweets = csv.reader(temp)
    for tweet in tweets:
        if "?" in tweet[1]:
            try:
                print tweet[1].encode('unicode_escape').decode('utf-8')
                cmd = raw_input("(1=question, 2=keep, 3=discard, 4=break): ")
                if cmd == "1":
                    data.append([3, tweet[1]])
                elif cmd == "2":
                    data.append([tweet[0], tweet[1]])
                elif cmd == "4":
                    break
            except Exception as e:
                break #will print and shit
                
            # if len(tweet[1]) > 50 and random.random() < 0.3333:
            #     text = tweet[1].replace(":))", "").replace(":)", "").replace(":P", "").replace(":-)", "").replace(": )", "").replace(":D", "").replace("=)", "").replace(":(", "").replace(":-(", "").replace(": (", "")
            #     data.append(['positive', text.encode('unicode_escape').decode('utf-8') + "\n"])
            # else:
            #     data.append(['positive', tweet[1].encode('unicode_escape').decode('utf-8') + "\n"])
        else:
            data.append([tweet[0], tweet[1]])

    wr = csv.writer(corpus, delimiter=',')
    wr.writerows(data)
    corpus.close()
    temp.close()
    print "DONE"

if __name__ == '__main__':
    main()