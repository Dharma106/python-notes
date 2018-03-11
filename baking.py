# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 23:39:36 2017

@author: KumarD1
"""
if __name__ =='__main__':
    import temperature_program

def get_preheating_instructions(fahrenheit):
    """ (number) -> string
    
    Return instructions for preheating the oven in fahrenheit and
    Celcius degrees.
    
    >>> get_preheating_instructions(500)
    'Preheat oven to 500 degrees F (260.0 degrees C).'
    """
    celc = str(temperature_program.convert_to_celcius(fahrenheit))
    fahr = str(fahrenheit)
    return 'Preheat oven to ' + fahr + ' degrees F (' + celc + ' degrees C).'


fahr = input("Enter the baking temperature in degree Fahrenheit: ")
print(get_preheating_instructions(fahr))
    
    
