# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:30:51 2017

@author: KumarD1
"""

def tinyfunction(x):
    print "testing how modules and interactive mode communicate"
    print  "You passed me the parameter", x
    
    z = x ** 2
    print x, "squared is", z
    return z

# To get the help on any module, use help() function.
# As an example we will use module math.
import math
help(math)
# To list out all the names of any module use dir() function.
dir(math)
# To get help on any function of a module, first one need to 
# to import that module then use help(module.function)
help(math.pow)

# Python Data types
    # 1. Numerice data type
        # int(), long(), float(), complex(), decimal.Decimal()
    # 2. Sequential data type
        # string, e.g 
x_str = "string type data is simply double quoted." 
type(x_str)

        # tuple, e.g.
x_tuple = ("a", "anything written between small bracket")
type(x_tuple)
        
        # list type data, e.g.
x_list = ["This", "is", "the", "way", "list type data" "is", "written"]
type(x_list)

# To make a dictionay with two key paramters
swallow_velocity  = {"European": "1956", "african": "69"}

# 'Set' stores multiple items of different type, but each itme in
# a set must be unique. One use of set is to find the unique items.
my_list = ['spam', 'lovely', 'spam', 'gloriouos', 'spam']


str.count('color', 'c')





