import string
import sys
from pathlib import Path
import pprint


def parsefile(filename):
    file = Path.cwd().joinpath(filename)
    # open file and parse content
    with open(file) as f:
        content = f.read().lower()
        words = content
        for sings in string.punctuation:
            words = words.replace(sings, '')

        words = words.replace('\n', ' ')
        words = words.split(' ')
        countingwords = {}
        for word in words:
            countingwords[word] = countingwords.get(word, 0) + 1

        sorted_words = sorted(countingwords.items(), key=lambda x: x[1], reverse=True)
        sorted_words = sorted_words[:5]
        pp = pprint.PrettyPrinter(width=20)
        pp.pprint(sorted_words)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
        parsefile(file)
    else:
        print("Missing file to parse, please give the file name and path relative to script.")
