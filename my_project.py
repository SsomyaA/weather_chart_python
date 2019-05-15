# Import all the framework

from csv import DictReader
import re
from datetime import datetime
from matplotlib.dates import date2num, num2date
import numpy as np


#Load Data
datetime_list, barpress_list = [], []
datetime_re = re.compile(r'[\d]{2,4}') # regex to convert date time into perticular format : In this case it will convert all the datetime string to individual item

for year in range(2012, 2016):
    
    fname = f'/Users/somyabiswal/Documents/Become a python Developer/Ex_Files_Code_Clinic_Python/Exercise Files/Ch01/resources/Environmental_Data_Deep_Moor_{year}.txt'
    print(f'Loading {year}')
    reader = DictReader(open(fname, 'r'), delimiter='\t')
    for row in reader:
        barpress_list.append(float(row['Barometric_Press']))
        datetime_list.append(date2num(datetime(*list(map(int, datetime_re.findall(row['date       time    ']))))))
.
# store 'barpress_list' and 'datetime_list' into numpy array to increase the spped of array operation
datetime_array = np.array(datetime_list)
barpress_aaray = np.array(datetime_list)

