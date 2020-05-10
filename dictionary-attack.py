import sys
import hashlib
import string
from itertools import chain, product


def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
                                                 for i in range(1, maxlength + 1)))


# Passwords in memory
with open("passwords.txt", "r") as f:
    passwords = set([line.strip() for line in f])

dictionary = set()
for line in sys.stdin:
    dictionary.add(line.strip())

# dictionary word
counter = 0
success = 0
for word in dictionary:
    dictionary_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
    counter += 1
    for password in passwords:
        if password == dictionary_hash:
            success += 1
            sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                word, password, counter))
    sys.stdout.write("Attempt : {}, Success : {}\r".format(
        counter, success))

# dictionary word + word
for word1 in dictionary:
    for word2 in dictionary:
        word_concat = word1 + word2
        dictionary_hash = hashlib.md5(
            word_concat.encode('utf-8')).hexdigest()
        counter += 1
        for password in passwords:
            if password == dictionary_hash:
                success += 1
                sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                    word_concat, password, counter))
    sys.stdout.write("Attempt : {}, Success : {}\r".format(
        counter, success))

# dictionary word + digit
for word in dictionary:
    for randomDigit in bruteforce(string.digits, 3):
        counter += 1
        attempt = word+randomDigit
        wordDigit_hash = hashlib.md5(attempt.encode('utf-8')).hexdigest()
        for password in passwords:
            if password == wordDigit_hash:
                success += 1
                sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                    attempt, password, counter))
        sys.stdout.write("Attempt : {}, Success : {}\r".format(
            counter, success))

# digit + dictionary word
for word in dictionary:
    for randomDigit in bruteforce(string.digits, 3):
        counter += 1
        attempt = randomDigit + word
        wordDigit_hash = hashlib.md5(attempt.encode('utf-8')).hexdigest()
        for password in passwords:
            if password == wordDigit_hash:
                success += 1
                sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                    attempt, password, counter))
        sys.stdout.write("Attempt : {}, Success : {}\r".format(
            counter, success))

# dictionary reversed word x2
for word in dictionary:
    reverseWord = word[::-1]
    doubleReverse = reverseWord + reverseWord
    dictionary_hash = hashlib.md5(doubleReverse.encode('utf-8')).hexdigest()
    counter += 1
    for password in passwords:
        if password == dictionary_hash:
            success += 1
            sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                doubleReverse, password, counter))
    sys.stdout.write("Attempt : {}, Success : {}\r".format(
        counter, success))

# dictionary word + reversed word
for word1 in dictionary:
    for word2 in dictionary:
        word_concat = word1 + word2[::-1]
        dictionary_hash = hashlib.md5(
            word_concat.encode('utf-8')).hexdigest()
        counter += 1
        for password in passwords:
            if password == dictionary_hash:
                success += 1
                sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                    word_concat, password, counter))
    sys.stdout.write("Attempt : {}, Success : {}\r".format(
        counter, success))
