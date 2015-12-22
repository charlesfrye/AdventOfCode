import sys
import string
from itertools import groupby

password = list(sys.argv[1])


def increment(password):
    ind = -1
    badLetters = ['o','i','l']
    if any([letter in badLetters for letter in password]):
        badLetters = [letter for letter in badLetters if letter in password]
        firstBad = min([password.index(letter) for letter in badLetters])
        password = password[0:firstBad] \
                    +[chr(ord(password[firstBad])+1)]\
                    +['a']*(len(password)-firstBad-1)
    while True:
        if password[ind] == 'z':
            password[ind] = 'a'
            ind -= 1
            continue
        letter = password[ind]
        password[ind] = chr(ord(letter)+1)
        return password


def hasIncreasing(password):
    out = False; numIncreasing = 3
    ords = [ord(char) for char in password]
    diffs = [a-b for a,b in zip(ords[1:],ords[0:-1])]
    return any([(diffs[idx:idx+numIncreasing-1]==[1,1])
            for idx in range(len(diffs)-numIncreasing+1)])

def hasBadLetter(password):
    badLetters = ['o','i','l']
    return any([letter in badLetters for letter in password])

def hasTwoDoubles(password):
    doubles = []
    for letter,groups in groupby(password,lambda x:x):
        if (len(list(groups))>1) and (letter not in doubles):
            doubles.append(letter)
        if len(doubles) > 1:
            return True
    return False

while True:
    password = increment(password)
    if hasBadLetter(password) or not hasIncreasing(password) \
            or not hasTwoDoubles(password):
        continue
    else:
        break

print(str(password))
