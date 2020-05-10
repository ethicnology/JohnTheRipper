import sys
import hashlib

# Passwords in memory
with open("passwords.txt", "r") as f:
    passwords = set([line.strip() for line in f])

dictionary = set()
for line in sys.stdin:
    dictionary.add(line.strip())

# Is any animal match ?
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

# Is any concat animals match ?
for word1 in dictionary:
    for word2 in dictionary:
        animal_concat = word1 + word2
        dictionary_hash = hashlib.md5(
            animal_concat.encode('utf-8')).hexdigest()
        counter += 1
        for password in passwords:
            if password == dictionary_hash:
                success += 1
                sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                    animal_concat, password, counter))
    sys.stdout.write("Attempt : {}, Success : {}\r".format(
        counter, success))
