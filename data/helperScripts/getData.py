import os, oauth2, json, csv, random

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key="xxx", secret="xxx")
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers )
    return content


def main():
    max_id = "753730647579963392"
    mydata = []
    count = 0
    while count < 100000:
        corpus = open('quscorpus.csv', 'ab')
        result = oauth_req("https://api.twitter.com/1.1/search/tweets.json?max_id="+max_id+"&q=%40apple%20OR%20%40microsoft%20OR%20tech%20OR%20virtual%20OR%20business%20OR%20election%20OR%20bank%20lang%3Aen%20%3F", 'xxx-xxx', 'xxx' )
        data = json.loads(result)
        if not 'statues' in data:
            print result
        tweets = data['statuses']
        # print data
        id = ""
        for tweet in tweets:
            # corpus.write(tweet['id_str']+',"'+tweet['text'].encode('unicode_escape').decode('utf-8').replace('"','""')+'"' + "\n")
            if len(tweet['text']) > 50 and random.random() < 0.75:
                text = tweet['text'].encode('unicode_escape').decode('utf-8').replace(":))", "").replace(":)", "").replace(":P", "").replace(":-)", "").replace(": )", "").replace(":D", "").replace("=)", "").replace(":(", "").replace(":-(", "").replace(": (", "")
                mydata.append(['question', text.encode('unicode_escape').decode('utf-8')])
            else:
                mydata.append(['question', tweet['text'].encode('unicode_escape').decode('utf-8')])
            count+=1
            id = tweet['id_str']

        print json.dumps(data['search_metadata'])
        print "---v"
        print "\n\n\n"
        print "id: "+id
        try:
            max_id = data['search_metadata']['next_results'].replace("?max_id=","").replace("&q=who%20OR%20what%20OR%20where%20OR%20when%20OR%20why%20OR%20how%20OR%20if%20OR%20are%20OR%20do%20OR%20should%20OR%20guess%20lang%3Aen%20%3F&include_entities=1", "")
        except Exception as e:
            max_id = str(int(id)-1)
        print max_id
        wr = csv.writer(corpus, delimiter=',')
        wr.writerows(mydata)
        corpus.close()
        mydata = []

    


if __name__ == '__main__':
    main()