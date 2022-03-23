# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"
crib_substring = ""
print(crib)

##Break the code via brute force search
engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="ABC",
                                plugs="AA BB CC DD")    # Initial rotor setting without using plugboards

count = 0    # Initial counter counting 
start = time.monotonic()    # beginning of the progress

for rotor1 in capitalLetters:
    for rotor2 in capitalLetters:
        for rotor3 in capitalLetters: 
            decrypt = engine.encipher(ShakesHorribleMessage[-201:])
            #print("Decoded Message:",decrypt)
            count += 1   # Add 1 to counter after which try of decrypt

            if decrypt.find("Hail Shakes!") != -1: 
                print("Count:", count)   # Print out how many counts needed to decrypt
                #Print the Decoded message
                print("Final:",decrypt)
                break       
               

end = time.monotonic()  # Get the value of the clock after decrypt
print("Time elapsed during the process:", end - start)  # Time running in sec

"""
Part 2d Estimate time taken for 1940s computer

15 + 16113 * 5 + 16112 * 1 + 1 * 4 + 2
= 15 + 80,565 + 16112 + 4 + 2
= 96,698

96,698 / 5000
= 19.3396 sec 


Part 2e:

Five rotors have 60 (5 * 4 * 3) possible combinations (key)
n(n+1) / 2 = 25(26) / 2 = 325 ways (plugboard)

Time elapsed during the process: 17.25
Count: 16113
16113 / 17.25 = 934.0869565217391 millisecond

934.0869565217391 * 60 * 325
= 18,214,695.65217391 / 1000    # Convert to sec
= 18,214.69565217391

# Cal how much longer
18,214.69565217391 - 17.25
= 18,197.44565217391 / 60   # Convert to min
= 303.2907608695652 mins
"""