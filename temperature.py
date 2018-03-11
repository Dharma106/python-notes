# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 22:36:11 2017

@author: KumarD1
"""

def convert_to_celcius(fahrenheit):
    """ (number) -> float
    
    Return the number of celcius degree equivalent to fahrenheit degree.
    
    >>> convert_to_celcius(75)
    23.88888888888889
    
    """   
    return (fahrenheit - 32.0) * 5.0 / 9.0
    
def above_freezing(celcius):
    """ (number) -> bool
    
    Retrun True iff temperature  celcius degree is above freezing.
    
    >>> above_freezing(5.2)
    True
    >>> above_freezing(-2)
    False
    """
    
    return celcius > 0

def is_longer(L1, L2):
    """ (list, list) -> bool
    Return Ture if and only if the length of L1 is longer than the
    length of L2.
    
    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3]
    
    """
    return len(L1) > len(L2)
 
    
    
    
    
    
    
    
    
    
