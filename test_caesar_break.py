# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

#message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 
#message = "Phhw Ph Lq Wkh Jdughq" # For testing 
message = "tffl"

#frequency of each letter
# letter = key; count = value
letter_counts = Counter(message)
print(letter_counts)    # Print the count of each element in string

#find max letter
maxFreq = -1
maxLetter = None
letter_counts[' '] = 0  # Don't count spaces zero count
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq) 
    maxLetter = max(letter_counts, key = letter_counts.get)  # Find max freq letter in the string 
print("Max Ocurring Letter:", maxLetter)


#right shift for encrypting and left shift for descripting.
#predict shift
#assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = (ord('e') - ord(maxLetter)) % 26    # ord() return unicode code point 
print("Predicted Shift:", shift)

totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict

for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        # Dictionary for encryption 
        letter = letters[index]
        keys[letter] = letters[(index + shift) % 26]
        # Dictionary for decryption 
        invkeys = {val: key for key, val in keys.items()}
    else: #uppercase
        # Dictionary for encryption 
        keys[letter] = letters[(index + shift) % 26 + 26]
        # Dictionary for decryption
        invkeys = {val: key for key, val in keys.items()}
print("Cypher Dict", keys)

#decrypt
decryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(keys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string

# Checking if message is the same as the encrypt message provided 
#Encrypt
encryptedMessage = []
for letter in decryptedMessage:
    if letter == ' ': #spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(invkeys[letter])
print("Encrypted Message:", ''.join(encryptedMessage)) #join is used to put list inot string
