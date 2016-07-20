import re

def testRegex(str):
    while str != "quit":
        print re.sub(r'(.)\1+', r'\1\1', str)
        str = raw_input('string: ')

if __name__ == '__main__':
    testRegex(raw_input('string: '))