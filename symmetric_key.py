#word
n = 5

def encrypt(word,n):
    result = ""
    for s in word:
        result += chr((ord(s) + n - 97) % 26 + 97)
    return result

def decrypt(cipher,n):
    res = ""
    for s in cipher:
        res+= chr((ord(s) - n - 97) % 26 + 97)
    return res

word = input("send random word bob : ")
cipher = encrypt(word, n)
print("CIPHERTEXT:", cipher)
print("DECRYPTED:", decrypt(cipher, n))
if word == decrypt(cipher, n):
    print("GOOD")
else:
    print("BAD")

#nonce - random number
"""    
import random
n=5

def encrypt(word,n):
    result=(nonce+n)/10
    return result

def decrypt(cipher,n):
    res=(cipher*10)-n
    return res

nonce=random.randint(0, 22)
cipher = encrypt(nonce, n)
print("CIPHERTEXT:", cipher)
print("DECRYPTED:", decrypt(cipher, n))
if nonce == decrypt(cipher, n):
    print("GOOD")
else:
    print("BAD")
    
"""

#time-stamp
"""
import time
n=5

def encrypt(word,n):
    result=(word+n)/10
    return result

def decrypt(cipher,n):
    res=(cipher*10)-n
    return(int(res))

ts=time.strftime('%H%M%S')
print(int(ts))
cipher = encrypt(int(ts), n)
print("CIPHERTEXT:", cipher)
print("DECRYPTED:", decrypt(cipher, n))
if int(ts) == decrypt(cipher, n):
    print("GOOD")
else:
    print("BAD")
    
"""

