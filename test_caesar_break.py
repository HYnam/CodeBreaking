# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 

#frequency of each letter
letter_counts = Counter(message)
print(letter_counts)    # Print the count of each element in string

#find max letter
maxFreq = -1
maxLetter = None
del letter_counts[' ']  # Don't count spaces 
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq) 
    maxLetter = max(letter_counts, key = letter_counts.get)  # Find max freq letter in the string 
print("Max Ocurring Letter:", maxLetter)


#right shift for encrypting and left shift for descripting.
#predict shift
maxLetter = "e"     #assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = #COMPUTE SHIFT HERE
print("Predicted Shift:", shift)
