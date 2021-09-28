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
data = csv.reader(f)
header = next(data)


mx = [0]*4
mx_station = ['']*4

label = ['유임승차', '유임하차', '무임승차', '무임하차']
for row in data:
    for i in range(4, 7+1):
        row[i] = int(row[i].replace(',',''))
        if row[i] > mx[i-4]:
            mx[i-4] = row[i]
            mx_station[i-4] = row[1]+'_'+row[3]+'역'
for i in range(4):
    print(f'{label[i]}: {mx_station[i]}, {mx[i]}명')