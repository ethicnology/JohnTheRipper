import sys
import string
import hashlib
from itertools import chain, product

# Charge passwords in memory
passwords = set()
for line in sys.stdin:
    if len(line.strip()) != 32:
        raise Exception("There is no MD5 hashes")
    else:
        passwords.add(line.strip())
# Test
test = hashlib.md5("abcd".encode('utf-8')).hexdigest()
passwords.add(test)


def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
                                                 for i in range(1, maxlength + 1)))


counter = 0
success = 0
for attempt in bruteforce(string.ascii_lowercase, 10):
    counter += 1
    bruteforce_hash = hashlib.md5(attempt.encode('utf-8')).hexdigest()
    for password in passwords:
        if password == bruteforce_hash:
            success += 1
            sys.stdout.write(
                "The password = {} match hash : {} after {} attempts\n".format(attempt, password, counter))
    sys.stdout.write("Attempt : {}, Success : {}, Current : {}, Hash : {}\r".format(
        counter, success, attempt, bruteforce_hash))
