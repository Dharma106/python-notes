# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 23:31:43 2017

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


fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
celcius = convert_to_celcius(fahrenheit)
if above_freezing(celcius):
    print("It is above freezing.")
else:
    print("It is below freezing.")