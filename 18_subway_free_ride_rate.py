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

mx = 0
rate = 0
mx_station = ''

for row in data:
    for i in range(4, 7+1):
        row[i] = int(row[i].replace(',',''))
    if row[6] != 0 :
        rate = round(row[6] / (row[4]+row[6]) * 100, 2)
        if rate > mx:
            mx = rate
            mx_station = row[1]+'_'+row[3]

print(f'무임승차가 가장 많은 곳은 \'{mx_station} (약 {mx}%)\'입니다.')

