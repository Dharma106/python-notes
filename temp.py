# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import print_function
def is_positive(x):
    """ (number) <- bool
    Return True iff x is positvie
    
    >>> is_positive(13)
    True
    >>> is_positive(-401)
    False
    """
    return x > 0

    
3 < 5 != True 
3 < 5 != False 

date = input("Enter a date in the format DD MTH YYYY: ")

#Nested if statements

value = input("Enter the pH value: ")
if len(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print(ph, "is acidic.")
    elif ph > 7.0:
        print(ph, "is basic.")
    else:
        print(ph, "is netural.")
else:
    print("No pH value was given.")
    


# Decision based on few criteria.
# if age < 45 and if bmi is less than < 22.0,
# risk is low else it is Medium
# if age >=  45 and bmi less than 22.o,
# risk is medium else it is high.


age = input(" What's your age? ")
bmi = input("What is you BMI? ")

young = age < 45 
slim = bmi < 22.0
if young:
    if slim:
        risk = 'low'
    else:
        risk = 'medium'
else:
    if slim:
        risk = 'medium'
    else:
        risk = 'high'
print("you have", risk, "risk of heart disease!")

# other way to right this
if young and slim:
     risk = "low"
elif young and not slim:
    risk = "medium"
elif not young and slim:
    risk = "medium"
elif not young and not slim:
    risk = "high"

# to see the content in this 
import this

# if we change the value of any object of any module then
# to get the original value we need to restart the shell and 
# then read the object/function

# Other way is using relaod function from imp module which resotre to 
# the defualt values of any variable.

import math
math.pi = 3

import imp
math = imp.reload(math)

# To get the help of the python inbuilt functions, one can type
dir(__builtins__)

# The general form of a method call is as follows:
    #<<expression>>.<<method_name>>(<<arguments>>)


velocities = [0.0, 9.81, 106.0, 179.0]
for velocity in velocities:
    print('Metric:', velocity, 'm/sec;',
          'Imperial:', velocity * 3.78, 'ft/sec')
    
for speed in velocities:
    print('Metric:', speed, 'm/sec.')

my_country = 'Sone ke Chidiya India'
for ch in my_country:
    if ch.isupper():
        print(ch)
    
    
# sum over range through for loop
total = 0
for i in range(1, 101):
    total = total + i

values = [4, 10, 3, 8, 6]
for i in range(len(values)):
    values[i] = values[i] * 2

# Processing Parallel list using indices
metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]
for i in range(len(metals)):
    print(metals[i], weights[i])
    
# Nested Loop
outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print(metal + halogen)

# 

def print_table(n):
    """ (int) -> NoneType
    
    Print the multiplication table for numbers 1 through n inclusive
    >>> print_table(5)
      1 2   3     4   5
    1 1 2   3     4   5
    2 2 4   6     8   10
    3 3 6   9     12  15
    4 4 8   12    16  20
    5 5 10  15    20  25
    """
    # the numbers to be include in table.
    numbers = list(range(1, n+1))
    
    for i in numbers:
        print('\t' + str(i), end = '') 
    print()
        
    # printing row number and row output
    for i in numbers:
        print(i, end = '')
        for j in numbers:
            print('\t' + str(i*j), end ='')
        print()

# Looping until a condition is reached i.e. While

play = 3
while play > 0:    
    print(play)
    play = play - 1
    
# Bacterial Growth 
time = 0
population = 1000; # initial population 
growth_rate = 0.21 # 21 % growth per minute
while population < 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1

print('It took', time, 'minutes for bacteria to double.')
print("The final populated bacteria was", round(population), '.')

        
# Use of Multivalued assignment to set up controls        
time, population, growth_rate = 0, 1000, 0.21    

while population != 2000:
    population = population + population * growth_rate
    print(round(population))
    time = time + 1
    
    