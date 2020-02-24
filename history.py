
# *** Spyder Python Console History Log ***
import time_series.py
os.curdir
import time_series
%clear
os.curdir(default_dir)
default_dir
import str

##---(Sun Mar 11 15:19:54 2018)---
%clear
import time_series
import os
os.chdir('.')
import time_series
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
        process_file(input_file)
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
import read_smallest
import urllib
url = 'http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
webpage= urllib.urlopen(url)
webpage
for line in webpage:
    line = line.strip()
    line = line.decode('utf-8')
    print(line)
import urllib.request
import urllib2.request
import urllib
urllib.urlretrieve(url, filename= "hopedale2.txt')
urllib.urlretrieve(url, filename= "hopedale2.txt")
time_series.skip_header('hopedale2.txt')
import time_series
time_series.skip_header('hopedale2.txt')
time_series.skip_header('hopedale1.txt')
time_series.skip_header('hopedale.txt')
time_series.process_file('hopedale.txt')
%clear
with open('hopedale2.txt', 'r') as inuput_file
with open('hopedale2.txt', 'r') as input_file
with open('hopedale.txt', 'r') as input_file
import os
os.curdir
os.chdir(".')
os.chdir(".")
with open('hopedale.txt', 'r') as input_file
%clear
pip install pandas
