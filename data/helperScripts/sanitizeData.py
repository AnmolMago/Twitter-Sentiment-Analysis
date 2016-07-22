import csv, re
from collections import OrderedDict

posC = csv.reader(open('data/raw/corpuses/poscorpus_raw.csv', 'rU'))
negC = csv.reader(open('data/raw/corpuses/negcorpus_raw.csv', 'rU'))
qusC = csv.reader(open('data/raw/corpuses/quscorpus_raw.csv', 'rU'))

fix = {
    '\\u2019': "'",
    '\\\u2026': "...",
    '\\u201c': '"',
    '\\u201d': "'",
    '\\\\n': ' ',# '\\n' => ' '
    '&lt;': '<',
    '&gt;': '>',
    '&amp;': '&',
}

def clean(text):
    for k, v in fix.iteritems():
        text = text.replace(k,v)
        text = text.replace(k[1:],v)
    #order is important
    text = text.lower().replace("rt ", "")#make lowercase and remove rts
    text = re.sub(r'(\\\\u[0-9a-z]+)|(\\u[0-9a-z]+)', '', text)#replace emojis \U23u8ufygcik ... note U lowercase
    text = re.sub(r'([0-9]+)', '', text)#remove numbers
    text = re.sub(r'(http[s]?:\/\/[^ \n]+)', '', text)#replace URLs
    text = re.sub(r'(@[0-9a-z_]+)', '_tempuser_', text)
    text = text.replace("_tempuser_: ", "")#from the rts
    text = text.replace("_tempuser_", "")
    text = text.replace('...', ' ')
    text = re.sub(r'([.,\"\*\&\-\^\+])', '', text)#remove periods, commas, quotes, asterisks, ampersand
    text = re.sub(r'(.)\1+', r'\1\1', text)#max 2 repeats (haaaappppppyyyyyyy => haappyy)
    text = text.replace("<3" , ":)").replace(":]",":)").replace(";]", ":)").replace(":))", ":)").replace(": )", ":)").replace(";)", ":)").replace(":d", ":)").replace(":-)", ":)").replace("=)", ":)").replace(":P", ":)")
    text = text.replace("</3", ":(").replace(":[",":(").replace(";[", ":(").replace(":((", ":(").replace(": (", ":(").replace(";(", ":(").replace("d:", ":(").replace(":-(", ":(").replace("=(", ":(").replace("=/", ":(").replace("=\\", ":(")
    text = re.sub(r'(?<!:)\)(?!:)', '', text)#remove '(' or ')' if not ':(' or '):'
    text = re.sub(r'([\\\/])', ' ', text)#replace '\' or '/' with ' '
    text = text.replace("!", " !")#makes exclamation marks their own word
    text = text.replace("?", " ?")#makes question marks their own word
    text = text.replace("#", "")#makes hashtags just word
    text = re.sub(' +',' ',text)#remove multiple consecutive spaces
    if text[0] == " ":
        text = text[1:]
    return text

def softClean():
    for corpus, abv in {posC: 'pos', negC: 'neg', qusC: 'qus',}.iteritems():
        data = []
        for row in corpus:
            data.append([row[0], clean(row[1]).rstrip()])
        f = open('data/clean/' + abv + 'corpus.csv', 'wb')
        wr = csv.writer(f)
        wr.writerows(data)
        print "done"

if __name__ == '__main__':
    print softClean()