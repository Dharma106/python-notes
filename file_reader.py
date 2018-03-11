# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 23:32:57 2018

@author: KumarD1
"""
#import urllib
#urllib.urlretrieve(url = 'http://proa.accuweather.com/adcbin/professional/historical_index.asp?location=VAAH%7CAKOLA%7CIN&Submit1=Get+Text' )
#import os
#os.chdir("C:/Users/kumard1/.spyder/file_examples")
file = open('file_example.txt', 'r')
contents = file.read()
print(contents)
file.close

# instead of calling "close" function seperately one can use with statement

with open('file_example.txt') as file:
    contents = file.read()
print contents

# Playing with read function
with open('file_example.txt', 'r') as example_file:
    firts_ten_chars= example_file.read(10)
    the_rest = example_file.read()
print("The first ten characters: ", firts_ten_chars)
print("The rest of the file:", the_rest)

# Reading text in the file as line using "readlines" function.
with open('file_example.txt', 'r') as example_file:
    lines = example_file.readlines()
print(lines)

with open('planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()
planets    
# To get the words in reversed order by using str "reversed" function
for planet in reversed(planets):
    print(planet.strip())

# To get the words in sorted order by using str "reversed" function
for planet in sorted(planets):
    print(planet.strip())
    
with open('planets.txt', 'r') as lines:
    for line in lines:
        print(len(line))

with open('hopedale.txt', 'r') as hopedale_file:
    hopedale_file.readline()
    data = hopedale_file.readline().strip()
    while data.startswith('#'):
        data = hopedale_file.readline().strip()
    total_pelts = int(data)
    for data in hopedale_file:
        total_pelts= total_pelts + int(data.strip())
    print("Total number of pelts:", total_pelts)
    
# using rstrip to remove the trailing whitespace.

with open('hopedale.txt', 'r') as hopedale_file:
    # Read the description of the file
    hopedale_file.readline()
    # keep reading the comment line until we encounter the first piece of data.
    data = hopedale_file.readline().rstrip()
    while data.startswith('#'):
        data = hopedale_file.readline().rstrip()
    print(data)
    
    for data in hopedale_file:
        print(data.rstrip())


import urllib
url = 'http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)
    


def sum_number_pairs(input_file, output_filename):
    """ (file open for reading, str) -> NoneType
    
    Read the data from input_file, which contains two floats per line
    seperated by a space. Open a file name output_file and, for each line in 
    input_file, write a line in the output file that contains two floats from
    the corresponding line of input_file and a space and the sum of the 
    two floats.
    
    """
    
    with open(output_filename, 'w') as output_file:
        for number_pair in input_file:
            number_pair = number_pair.strip()
            operand = str.split(number_pair)
            total= float(operand[0]) + float(operand[1])
            new_line = '{0} {1}\n'.format(number_pair, total)
            output_file.write(new_line)
            
            
            































