# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:58:31 2017

@author: KumarD1
"""

for miles in range(10, 70, 10):
    km = miles * 1.609
    print "%d miles ==> %3.2f kilometers" % (miles, km)
    
def foo():
    return 1
 
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
my_list
set(my_list)



# Calling a method examples
zed = "lowercase string"
# To use method, structure is defined as 
# type the name, a dot, the method name, and a set of Paranthesis.
zed.upper() 
# paranthesis after method ask python to call that method.
'hi'.upper()
# parenthesis after method is sometimes used with arguments for other need.
shopping_list = ['eggs', 'bacon', 'spam']
shopping_list.append('butter')

# Python tests an expression with and and or operators from left to right
# and returns the last value tested. Examples
'1' and 1 and 'one' # will result with one not as TRUE or FALSE

# True and False comes only when exprssion uses comparison operators.
(2 < 3) or (4 > 5)

# Note: In python false has a special meaning.
# It refers to anything that is zero or "empty."
# Conditional Operations
X = 2; C = False; Y = 2
X if C else Y

# Here first C is evaluated. If C is true, then X is evaluated
# to give the resule. Otherwise, Y is evaluate to give the result
    # False evaluates as false

print 'foo' if False else 'bar' 

live_parrot = "'E's pinin' for the fjords!" # Michael Palin
 
# Understanding Indention in Python through if 

statement = "I didn't get anything from this statements."
response = " what is this?"
if statement == "We're fresh out of red Leichester, sir":
    response = "Oh, never mind, how are you on Tilset?"
elif statement == "We have cammebert, yes sir":
    response = "Fetch hither the fromage de la Belle France!"
else:
    response = "I'm going to have to shoot you."

# For loop example
little_list = ["the", "quick", "brown", "fox"]
for item in little_list:
    print item, "*",

# While loop repeats an instruction as long as a particular condition is true.
# An example
countdown = 10
while countdown:
    print countdown,
    countdown = countdown - 1
print "blastoff!"

# About Try and related statements
user_input = raw_input("Enter an integer: ")
try:
    number = int(user_input)
    print "You entered", number
except ValueError:
    print "Integers, please!"    
     
# Playing with join function
music = ["Abba", "Rolling Stones", "Black Sabbath", "Metallica"]
print ' '.join(music)
print "    ".join(music)

# ABout Namespace
def myfunction(x):
    y = x**x
    print x,"raised to the power of",x,"is", y
    return y

# Classes
class SayMyName:
    def __init__(self, myname):
        self.myname = myname
    def say(self):
        print "Hello, my name is",self.myname
# Classes are useful because it combine both data and methods. 
# Python data types- list, strings, tupel and many more are based 
# on the classes.

        
# Python Language full example.



import sys
import urllib2
import urlparse
import htmllib, formatter
from cStringIO import StringIO

def log_stdout(msg):
    """Print msg to screen."""
    print msg   
    
    
def get_page(url, log):
    """Retrieve URL and return contents, log errors."""
    try:
        page = urllib2.urlopen(url)
    except urllib2.URLError:
        log("Error reteriving: " + url)
    return ''
    body = page.read()
    page.close()
    return body



    