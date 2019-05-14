# Import all the framework

from csv import DictReader

fname = '/Users/somyabiswal/Documents/Become a python Developer/Ex_Files_Code_Clinic_Python/Exercise Files/Ch01/resources/Environmental_Data_Deep_Moor_2012.txt'

reader = DictReader(open(fname, 'r'), delimiter='\t')

for row in reader:
    print(row['date       time    '])
