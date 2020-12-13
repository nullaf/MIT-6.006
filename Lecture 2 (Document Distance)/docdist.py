import math
import string
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: docdist.py filename1 filename2")
    else:
        doc1 = sys.argv[1]
        doc2 = sys.argv[2]
        freq_map1 = wordFrequenciesForFile(doc1)
        freq_map2 = wordFrequenciesForFile(doc2)
        distance = vectorAngle(freq_map1, freq_map2)
        print(f"The distance between documents: {distance} (Radians)")


def readFile(filename):
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print(f"Error opening or reading input file: {filename}")
        sys.exit()


def getWordsFromText(text):
    text = text.translate(text.maketrans(string.punctuation + string.ascii_uppercase,
                                         " " * len(string.punctuation) + string.ascii_lowercase))
    wordList = text.split()
    return wordList


def countFrequency(wordlist):
    D = dict()
    for newWord in wordlist:
        if newWord in D:
            D[newWord] = D[newWord] + 1
        else:
            D[newWord] = 1
    return D


def wordFrequenciesForFile(filename):
    lineList = readFile(filename)
    wordList = getWordsFromText(' '.join(lineList))
    freqMap = countFrequency(wordList)
    return freqMap


def innerProduct(d1, d2):
    result = 0
    for key in d1:
        if key in d2:
            result += d1[key] * d2[key]
    return result


def vectorAngle(d1, d2):
    numerator = innerProduct(d1, d2)
    denominator = math.sqrt(innerProduct(d1, d1) * innerProduct(d2, d2))
    return math.acos(numerator / denominator)


main()
