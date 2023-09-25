import string
import pprint


def string_to_list(text):
    word_list = [text.strip(string.punctuation)
                 for text in text.lower().split()]
    return word_list


def count_words_in_list(words, cache):
    for word in words:
        if word in cache:
            # print('Adding to word counter')
            cache[word] = cache[word] + 1
        else:
            # print('Creating word counter')
            cache[word] = 1


def count_words_in_file(filepath):
    word_cache = dict()

    file_in = open(filepath)

    for line in file_in:
        word_list = string_to_list(line)
        count_words_in_list(word_list, word_cache)

    file_in.close()
    return word_cache


# print(count_words_in_file('test_text.txt'))
pp = pprint.PrettyPrinter()
pp.pprint(count_words_in_file('test_text.txt'))
