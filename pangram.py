#Strings, Lists, Slicing, Iteration

import string
def is_pangram(sentence):
    MyVariable = sentence.lower()
    Alphabet = string.ascii_lowercase
    for letter in Alphabet:
        if letter not in MyVariable:
            return False
    return True

from string import ascii_lowercase as alphabet

def is_pangram(sentence):
    return set(alphabet).issubset(set(sentence.lower()))
