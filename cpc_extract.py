# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:03:54 2017

@author: Rajasivaranjan
email:   rajasivaranjan92@gmail.com

"""

import os
import urllib

os.chdir("C:/Users/kumard1/.spyder")
lines = open('CPC_Precipitation_ForecastMaps_files.txt').read().splitlines()
j = 1
for i in lines:
    print(urllib.urlretrieve(i, str(j).zfill(3)+"_"+i.split("/")[-1]))
    j=j+1