#An API that encrypts and decrypts code
from bindec import *

def charToBin(c):
#converts a character into a list of six 1's and 0's using Base64 encoding
    if c.isupper():
        integ = ord(c) - 65
        return(decToBin(integ))
            
    elif c.islower():
          integ = ord(c) - 71
          return(decToBin(integ))

    elif c == "/":
        integ1 = 63
        return(decToBin(integ))

    elif c == "+":
        integ = 62
        return(decToBin(integ))
            


def binToChar(b):
#converts a list of six 1's and 0's into a character using Base64 encoding
    dec = binToDec(b)
    
    if dec <= 25:
        dec += 65
        char = chr(dec)
        return(char)

    elif dec > 25:
        dec += 71
        char = chr(dec)
        return(char)

    elif dec == 62:
        char = chr(43)
        return(char)

    elif dec == 63:
        char = chr(47)
        return(char)

    
    
def strToBin(s):
#converts a string of characters into a list of 1's and 0's using Base64 encoding
    lst=[]
    for c in s:
        lst += (charToBin(c))
    return lst


def binToStr(b_list):
#convert a list of 1's and 0's into a string of characters using Base64 encoding
    i = 0
    j = 6
    string = ""
    count = 0
    for x in b_list:
        count += 1
    count = count//6
    
    for x in range(0,count):
        arr = b_list[i:j]
        k = binToChar(arr)
        string += k
        i += 6
        j += 6
    return string


def generatePad(seed, k, l):
#returns a pseudo-random list of 1s and 0s, generated by an [N, k] LFSR, where N = length of seed
    toReturn = ""
    lfsr = []
    for j in range(l):
        if int(seed[0]) == int(seed[len(seed)-k]): toReturn += "0"
        else:
            toReturn += "1"
        seed = seed[1:]
        seed.append(toReturn[-1])
    for i in toReturn:
        lfsr.append(int(i))
    return lfsr


def encrypt(message, seed, k):
#takes a string message and returns it as an encrypted string using an [N, k] LFSR
    msg = strToBin(message)
    code = generatePad(seed, k, len(msg))
    passw =[]
    for x in range(len(msg)):
        if msg[x] == code[x]:
            passw.append(0)
        else:
            passw.append(1)
    encrypted = binToStr(passw)
    return encrypted
            
        
            
    