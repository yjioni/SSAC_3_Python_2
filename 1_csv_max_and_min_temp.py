import csv
from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(
                        title='choose csv file',
                        initialdir='C:/Users/',
                        filetypes=(('csv files', '*.csv'),
                                    ('all files', '*.*'))
                        )

f = open(root.filename, 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)

max_temp = -999
max_date = ''
min_temp = 999
min_date = ''

for row in data:
    if row[-1] == '':
        row[-1] = -999
    row[-1] = float(row[-1])
    if max_temp < row[-1]:
        max_temp = row[-1]
        max_date = row[0]
    
    if row[-2] == '':
        row[-2] = 999
    row[-2] = float(row[-2])
    
    if min_temp > row[-2]:
        min_temp = row[-2]
        min_date = row[0]

f.close()
print('max_date: {}, max_temp: {}'.format(max_date, max_temp))
print('min_date: {}, min_temp: {}'.format(min_date, min_temp))