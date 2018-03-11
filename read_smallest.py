# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 15:22:33 2018

@author: KumarD1
"""

import os
os.chdir('C:\Users\\kumard1\\.spyder')

import time_series

def smallest_value(reader):
    """(file open for reading) -> NoneType
    
    Read and process reader and return the smallest value after the 
    time_series header.
    """
    line = time_series.skip_header(reader).strip()
    
    # Now line contains the first value which is also the smallest value
    # found so far, because it is the only one it has read.
    smallest = line
    
    for line in reader:
        value = int(line.strip())
        
        # if we find the smallest value rember it
        if value < smallest:
            smallest = value
        
    return smallest

if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))


    
    
    