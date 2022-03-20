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
                                rotor.ROTOR_II, rotor.ROTOR_III, key="AAA",
                                plugs="AA BB CC DD")

for engine.rotor1 in capitalLetters:
    for engine.rotor2 in capitalLetters:
        for engine.rotor3 in capitalLetters: 
            #startPos = engine.rotor1 + engine.rotor2 + engine.rotor3    # Generate a possible rotor start position
            #key = startPos  #Set starting position 
            decrypt = engine.encipher(ShakesHorribleMessage[-201:])
            print("Decoded Message:",decrypt)

            if decrypt == crib:
                #Print the Decoded message
                print("Decoded Message:",engine.encipher(ShakesHorribleMessage))
