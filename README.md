# JohnTheRipper

## Tkinter GUI

How to use JohnTheRipper.py :

```sh
python3 JohnTheRipper.py
```

Then you should copy & paste animals.txt, passwords.txt, users.txt in their respective text boxes :  
![alt text](https://github.com/ethicnology/JohnTheRipper/blob/master/screenshot.png "JohnTheRipper")

### Bruteforce

How to use bruteforce.py :

```sh
cat passwords.txt | python3 bruteforce.py
```

Expected output :

```sh
The password = abcd match hash : e2fc714c4727ee9395f324cd2e7f331f after 19010 attempts
```

### Dictionary

How to use dictionary-attack.py :

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
```

### Simple

How to use simple.py :

```sh
cat users.txt | python3 simple-attack.py
```

Expected output :

```sh
The password = 167vivien match hash : 54fd8fb2eaf6b40ecd347713770e83d5 after 33608 attempts
The password = ViNcEnT match hash : 4eb01b0c1900c192da5c2aba253de3c0 after 666607 attempts
```
