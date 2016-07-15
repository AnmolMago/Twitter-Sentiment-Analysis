import csv

data = []

def find_duplicates(f):
    seen = set()
    # for line in f:
    #     line_lower = line.lower()
    #     if line_lower in seen:
    #         print(line)
    #     else:
    #         seen.add(line_lower)
    words = csv.reader(f)
    count = 0

    for word in words:
        if word[0].lower() in seen:
            print(word[0])
            count += 1
        else:
            seen.add(word[0].lower())
    print count

def truncate(f, n):
    '''Truncates a float f to n decimal places without rounding'''
    if len(str(f).split('.')[1]) < n:
        return f
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def fix_duplicates(f):
    current = ""
    rows = csv.reader(f)
    pos = 0.0
    neg = 0.0
    count = 0
    for row in rows:
        if row[0].lower() == current:
            pos += float(row[1])
            neg += float(row[2])
            count += 1
        else:
            if current != "":
                data.append([current, truncate(pos/count, 4), truncate(neg/count, 4), truncate(1 - (pos/count + neg/count), 4)])
            current = row[0].lower()
            pos = float(row[1])
            neg = float(row[2])
            count = 1
    for row in data:
        if row[0] == "cool":
            print row
    corpus = open('../SentiWordNet_reformatted.csv', 'wb')
    wr = csv.writer(corpus, delimiter=',')
    wr.writerows(data)
    corpus.close()



if __name__ == '__main__':
    with open('../SentiWordNet_reformatted.csv') as f:
        fix_duplicates(f)