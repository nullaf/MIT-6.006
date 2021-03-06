import math
import string
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: docdist.py filename1 filename2")
    else:
        doc1 = sys.argv[1]
        doc2 = sys.argv[2]
        freq_map1 = word_frequencies_for_file(doc1)
        freq_map2 = word_frequencies_for_file(doc2)
        distance = vector_angle(freq_map1, freq_map2)
        print(f"The distance between documents: {distance} (Radians)")


def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print(f"Error opening or reading input file: {filename}")
        sys.exit()


def get_words_from_text(text):
    text = text.translate(text.maketrans(string.punctuation + string.ascii_uppercase,
                                         " " * len(string.punctuation) + string.ascii_lowercase))
    word_list = text.split()
    return word_list


def count_frequency(word_list):
    d = dict()
    for newWord in word_list:
        if newWord in d:
            d[newWord] = d[newWord] + 1
        else:
            d[newWord] = 1
    return d


def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_text(' '.join(line_list))
    freq_map = count_frequency(word_list)
    return freq_map


def inner_product(d1, d2):
    result = 0
    for key in d1:
        if key in d2:
            result += d1[key] * d2[key]
    return result


def vector_angle(d1, d2):
    numerator = inner_product(d1, d2)
    denominator = math.sqrt(inner_product(d1, d1) * inner_product(d2, d2))
    return math.acos(numerator / denominator)


main()
