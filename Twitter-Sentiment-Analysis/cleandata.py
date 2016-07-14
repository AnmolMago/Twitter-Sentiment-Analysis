import os, csv, oauth2, json, codecs

def getLines():
    f = open('corpus.csv', 'r')
    count = 0
    line = ""
    lines = []
    try:
        reader = csv.reader(f)
        for row in reader:
            if count >= 100:
                lines.append(line)
                count = -1
                line = ""
            elif row[2] != "":
                if count == 0:
                    line += row[2]
                else: 
                    line += ("," + row[2]) 
            count += 1
    finally:
        lines.append(line)
        f.close()
        print("total of " + str(len(lines)) + " lines, " + str(count) + " on the last line")
        return lines

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key="xxx", secret="xxx")
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers )
    return content

def main():
    lines = getLines()
    #there has got to be a better way to do this.... oh well
    raw = codecs.open('rawdata.txt', encoding='utf-8')
    f = open('corpus.csv','r')
    filedata = f.read().decode('utf-8')
    f.close()
    for line in lines:
        line = line.decode('utf-8')
        result = oauth_req("https://api.twitter.com/1.1/statuses/lookup.json?id="+line, 'xxx', 'xxx' )#100 tweets at a time
        tweets = json.loads(result)
        
        for tweet in tweets:
            id = tweet['id_str'].decode('utf-8')
            text = tweet['text'].encode('unicode_escape').decode('utf-8')
            filedata = filedata.replace(id,text).decode('utf-8')

    f = open('corpusnew.csv','w')
    f.write(filedata.encode('utf-8'))
    f.close()


if __name__ == '__main__':
    main()