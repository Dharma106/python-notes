# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 10:40:13 2018

@author: KumarD1
"""

from __future__ import print_function
#text = ''
#while text != 'quit':
#    text = input("Please enter a chemical formula (or 'quit' to exit): ")
#    if text == "quit" :
#        print("...exiiting program")
#    elif text == "H2O" :
#        print("Water")
#    elif text == "NH3" :
#        print("Ammonia")
#    elif text == "CH4" :
#        print("Methane")
#    else:
#        print("Unkonwn Compound")
        
while True:
    text =input("Enter a chemical formula (or 'quit' to exit): ")
    if text ==  "quit":
        print("...exiting program")
        break
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown Compound")
        
# this method continues to run loop till end,
# even when it satisfy the condition.         
s = 'C3H7'
digit_index = -1
for i in range(len(s)):
    if digit_index == -1 and s[i].isdigit():
        digit_index = i

# Using break function to come out of loop once,
# it reach the first encounter.
s = 'C3H7'
digit_index = -1
for i in range(len(s)):
    if s[i].isdigit():
        digit_index = i
        break

# Use of continue function in Looping
sn = 'D1H0A6MA'
total = 0 # the sum of the digits seen so far.
count = 0 # number of digits seen so far
for i in range(len(sn)):
    if sn[i].isalpha():
        continue
    total = total + int(sn[i])
    count = count + 1
 

# Chapter 9 Exercise practice

celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
for i in range(len(celegans_phenotypes)):
    print(celegans_phenotypes[i])
    
half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
for i in range(len(half_lives)):
    print(half_lives[i], end = '\t')
 
max_row = 7
char = 'T'
for i in range(max_row + 1):
    req_char = char * i
    print(req_char)

    
                 