# Import all the framework

from csv import DictReader
import re
from datetime import datetime
import matplotlib
from matplotlib.dates import date2num, num2date
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from tkinter import *
from tkinter import ttk, messagebox


class WeatherStatistics:
    def __init__(self, master):
        
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

        # store 'barpress_list' and 'datetime_list' into numpy array to increase the spped of array operation
        
        '''
        Testing Data without loading the txt value
        self.datetime_array = np.array(datetime_list)
        self.barpress_aaray = np.array(datetime_list)
        '''

        self.datetime_array = [734503.00155093, 734503.0058912, 734503.01024306, 735753.0446875, 735753.0465162,  735753.04815972]
        # Build the GUI
        master.title('Weather Statistics')
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (w, h))

        matplotlib.rc('font', size = 18)
        f = Figure()
        f.set_facecolor((0,0,0,0))
        self.a = f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(f, master)
        self.canvas.draw()
        toolbar_frame = ttk.Frame(master) # needed to put navbar above plot
        toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        toolbar.update()
        toolbar_frame.pack(side=TOP, fill=X, expand=0)
        self.canvas._tkcanvas.pack(fill=BOTH, expand=1)

        controls_frame = ttk.Frame(master)
        controls_frame.pack()

        # Start Field Design and Configuration
        ttk.Label(controls_frame, text = 'Start', font= 'Arial 18 bold').grid(row=0, column=0, pady=5)
        ttk.Label(controls_frame, text = '(YYYY-MM-DD HH:MM:SS)', font='Courier 12').grid(row=1, column=0, padx=50, sticky='s')
        self.start = StringVar()
        ttk.Entry(controls_frame, width = 19, textvariable = self.start, font = 'Courier 12').grid(row = 2, column = 0, sticky='n')
        self.start.set(str(num2date(self.datetime_array[0]))[0:19])

       

        # End Field Design and Configuration
        ttk.Label(controls_frame, text = 'End', font='Arial 18 bold').grid(row=0, column=1, pady=5)
        ttk.Label(controls_frame, text = '(YYYY-MM-DD HH:MM:SS)', font='Courier 12').grid(row=1, column=1, padx=50, sticky='s')
        self.end = StringVar()
        ttk.Entry(controls_frame, width = 19, textvariable=self.end, font='Courier 12').grid(row=2, column=1, sticky='n')
        self.end.set(str(num2date(self.datetime_array[-1]))[0:19])
        



       

def main():
    root = Tk()
    app = WeatherStatistics(root)
    root.mainloop()

if __name__ == '__main__':
    main()
