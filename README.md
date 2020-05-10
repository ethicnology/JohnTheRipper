# JohnTheRipper

## Bruteforce

How to use bruteforce.py :

```sh
cat passwords.txt | python3 bruteforce.py
```

Expected output :

```sh
The password = abcd match hash : e2fc714c4727ee9395f324cd2e7f331f after 19010 attempts
Current : edkqn, Hash : 4a27c0f91af1824866b3479f82a81348
```

## Dictionary

How to use bruteforce.py :

```sh
cat animals.txt | python3 dictionary-attack.py
```

Expected output :

```sh
The password = hippocampe match hash : a409f32fef1cc24d4fbe7256accf8eb9 after 45 attempts
The password = chatchien match hash : 14bfcc4be324181b91812b0b2f70ce40 after 31449 attempts
The password = marsouin89 match hash : a9b0cd97f83f9251411af4b5f1f0bd59 after 72232 attempts
The password = 673crabe match hash : 8699fc754c2e40dc7ef0ca9634b92d17 after 461416 attempts
The password = nipalnipal match hash : 42167255eb290439c4200edfe3639ab5 after 620610 attempts
Attempt : 683724, Success : 5
```
