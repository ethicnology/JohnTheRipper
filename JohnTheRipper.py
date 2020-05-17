import sys
import string
import hashlib
from itertools import chain, product


def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
                                                 for i in range(1, maxlength + 1)))


class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.insert('end', string)
        self.text_space.see('end')


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class Interface(tk.Frame):
    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=945, height=519, **kwargs)
        self.pack(fill=tk.BOTH)
        self.nb_clic = 0

        self.TextDictionary = tk.Text()
        self.TextDictionary.place(relx=0.669, rely=0.031,
                                  relheight=0.293, relwidth=0.312)

        self.TextDictionary.configure(background="white")
        self.TextDictionary.configure(font="TkTextFont")
        self.TextDictionary.configure(foreground="black")
        self.TextDictionary.configure(highlightbackground="#d9d9d9")
        self.TextDictionary.configure(highlightcolor="black")
        self.TextDictionary.configure(insertbackground="black")
        self.TextDictionary.configure(selectbackground="#c4c4c4")
        self.TextDictionary.configure(selectforeground="black")
        self.TextDictionary.configure(undo="1")
        self.TextDictionary.configure(wrap="word")

        self.TextUsers = tk.Text()
        self.TextUsers.place(relx=0.018, rely=0.031,
                             relheight=0.293, relwidth=0.308)

        self.TextUsers.configure(background="white")
        self.TextUsers.configure(font="TkTextFont")
        self.TextUsers.configure(foreground="black")
        self.TextUsers.configure(highlightbackground="#d9d9d9")
        self.TextUsers.configure(highlightcolor="black")
        self.TextUsers.configure(insertbackground="black")
        self.TextUsers.configure(selectbackground="#c4c4c4")
        self.TextUsers.configure(selectforeground="black")
        self.TextUsers.configure(undo="1")
        self.TextUsers.configure(wrap="word")

        self.Button1 = tk.Button()
        self.Button1.place(relx=0.035, rely=0.345, height=24, width=107)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Simple''')
        self.Button1.configure(command=self.simple)

        self.Button2 = tk.Button()
        self.Button2.place(relx=0.405, rely=0.345, height=24, width=107)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Dictionary''')
        self.Button2.configure(command=self.dictionary)

        self.Button3 = tk.Button()
        self.Button3.place(relx=0.775, rely=0.345, height=24, width=107)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Bruteforce''')
        self.Button3.configure(command=self.forcebrute)

        self.console_area = tk.Text()
        self.console_area.place(relx=0.0, rely=0.47,
                                relheight=0.545, relwidth=1.011)
        self.console_area.configure(background="white")
        self.console_area.configure(font="TkTextFont")
        self.console_area.configure(foreground="black")
        self.console_area.configure(highlightbackground="#d9d9d9")
        self.console_area.configure(highlightcolor="black")
        self.console_area.configure(insertbackground="black")
        self.console_area.configure(selectbackground="#c4c4c4")
        self.console_area.configure(selectforeground="black")
        self.console_area.configure(undo="1")
        self.console_area.configure(wrap="word")

        self.TextHashes = tk.Text()
        self.TextHashes.place(relx=0.347, rely=0.031,
                              relheight=0.295, relwidth=0.306)

        self.TextHashes.configure(background="white")
        self.TextHashes.configure(font="TkTextFont")
        self.TextHashes.configure(foreground="black")
        self.TextHashes.configure(highlightbackground="#d9d9d9")
        self.TextHashes.configure(highlightcolor="black")
        self.TextHashes.configure(insertbackground="black")
        self.TextHashes.configure(selectbackground="#c4c4c4")
        self.TextHashes.configure(selectforeground="black")
        self.TextHashes.configure(undo="1")
        self.TextHashes.configure(wrap="word")

        self.Label1 = tk.Label()
        self.Label1.place(relx=0.138, rely=-0.01, height=21, width=68)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Users''')

        self.Label2 = tk.Label()
        self.Label2.place(relx=0.466, rely=-0.01, height=21, width=67)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Passwords''')

        self.Label3 = tk.Label()
        self.Label3.place(relx=0.783, rely=-0.01, height=21, width=59)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Dictionary''')

    def simple(self):
        hashesInput = self.TextHashes.get("1.0", 'end-1c')
        hashesArray = hashesInput.split("\n")
        passwords = set()
        for line in hashesArray:
            passwords.add(line.strip())

        usersInput = self.TextUsers.get("1.0", 'end-1c')
        usersArray = usersInput.split("\n")
        users = set()
        for line in usersArray:
            users.add(line.strip())

        counter = 0
        for user in users:
            user = user.lower()
            # user + digit
            for randomDigit in bruteforce(string.digits, 4):
                counter += 1
                attempt = user+randomDigit
                wordDigit_hash = hashlib.md5(
                    attempt.encode('utf-8')).hexdigest()
                for password in passwords:
                    if password == wordDigit_hash:
                        sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                            attempt, password, counter))
            # digit + user
            for randomDigit in bruteforce(string.digits, 4):
                counter += 1
                attempt = randomDigit + user
                wordDigit_hash = hashlib.md5(
                    attempt.encode('utf-8')).hexdigest()
                for password in passwords:
                    if password == wordDigit_hash:
                        sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                            attempt, password, counter))

        for user in users:
            user = user.lower()
            user = user.capitalize()
            #user + digit
            for randomDigit in bruteforce(string.digits, 4):
                counter += 1
                attempt = user+randomDigit
                wordDigit_hash = hashlib.md5(
                    attempt.encode('utf-8')).hexdigest()
                for password in passwords:
                    if password == wordDigit_hash:
                        sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                            attempt, password, counter))
            # digit + user
            for randomDigit in bruteforce(string.digits, 4):
                counter += 1
                attempt = randomDigit + user
                wordDigit_hash = hashlib.md5(
                    attempt.encode('utf-8')).hexdigest()
                for password in passwords:
                    if password == wordDigit_hash:
                        sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                            attempt, password, counter))

        # UsEr
        new_users = []
        for user in users:
            char_list = []
            for i in range(len(user)):
                if i % 2 == 0:
                    char_list.append(user[i].upper())
                else:
                    char_list.append(user[i].lower())
            new_users.append(''.join(char_list))

        for new_user in new_users:
            new_user_hash = hashlib.md5(new_user.encode('utf-8')).hexdigest()
            counter += 1
            for password in passwords:
                if password == new_user_hash:
                    sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                        new_user, password, counter))

    def dictionary(self):
        hashesInput = self.TextHashes.get("1.0", 'end-1c')
        hashesArray = hashesInput.split("\n")
        passwords = set()
        for line in hashesArray:
            passwords.add(line.strip())

        dictionaryInput = self.TextDictionary.get("1.0", 'end-1c')
        dictionaryArray = dictionaryInput.split("\n")
        dictionary = set()
        for line in dictionaryArray:
            dictionary.add(line.strip())

        # dictionary word
        counter = 0
        for word in dictionary:
            dictionary_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
            counter += 1
            for password in passwords:
                if password == dictionary_hash:
                    sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                        word, password, counter))

        # dictionary word + word
        for word1 in dictionary:
            for word2 in dictionary:
                word_concat = word1 + word2
                dictionary_hash = hashlib.md5(
                    word_concat.encode('utf-8')).hexdigest()
                counter += 1
                for password in passwords:
                    if password == dictionary_hash:
                        sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                            word_concat, password, counter))

        # dictionary word + digit
        for word in dictionary:
            for randomDigit in bruteforce(string.digits, 3):
                counter += 1
                attempt = word+randomDigit
                wordDigit_hash = hashlib.md5(
                    attempt.encode('utf-8')).hexdigest()
                for password in passwords:
                    if password == wordDigit_hash:
                        sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                            attempt, password, counter))

        # digit + dictionary word
        for word in dictionary:
            for randomDigit in bruteforce(string.digits, 3):
                counter += 1
                attempt = randomDigit + word
                wordDigit_hash = hashlib.md5(
                    attempt.encode('utf-8')).hexdigest()
                for password in passwords:
                    if password == wordDigit_hash:
                        sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                            attempt, password, counter))

        # dictionary reversed word x2
        for word in dictionary:
            reverseWord = word[::-1]
            doubleReverse = reverseWord + reverseWord
            dictionary_hash = hashlib.md5(
                doubleReverse.encode('utf-8')).hexdigest()
            counter += 1
            for password in passwords:
                if password == dictionary_hash:
                    sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                        doubleReverse, password, counter))

        # dictionary word + reversed word
        for word1 in dictionary:
            for word2 in dictionary:
                word_concat = word1 + word2[::-1]
                dictionary_hash = hashlib.md5(
                    word_concat.encode('utf-8')).hexdigest()
                counter += 1
                for password in passwords:
                    if password == dictionary_hash:
                        sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                            word_concat, password, counter))

    def forcebrute(self):
        hashesInput = self.TextHashes.get("1.0", 'end-1c')
        hashesArray = hashesInput.split("\n")
        passwords = set()
        for line in hashesArray:
            passwords.add(line.strip())

        counter = 0
        # string.ascii_letters = lower and upper & string.digits = 0123456789
        for attempt in bruteforce(string.ascii_letters+string.digits, 3):
            counter += 1
            bruteforce_hash = hashlib.md5(attempt.encode('utf-8')).hexdigest()
            for password in passwords:
                if password == bruteforce_hash:
                    sys.stdout.write(
                        "The password = {} match hash : {} after {} attempts\n".format(attempt, password, counter))


fenetre = tk.Tk()
interface = Interface(fenetre)
sys.stdout = StdoutRedirector(interface.console_area)
interface.mainloop()
interface.destroy()
