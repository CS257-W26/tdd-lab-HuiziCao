'''
A file for the production code
'''

import sys

def reverse_word(word):
    return word[::-1]

def reverse_all_words(phrase):
    return " ".join(reverse_word(w) for w in phrase.split())
