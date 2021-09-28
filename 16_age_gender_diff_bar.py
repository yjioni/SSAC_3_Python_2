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

# '2021년08월_남_100세 이상' 103
# '2021년08월_여_0세' 106

name = input('읍면동 >:')

diff = []

for row in data:
    if name in row[0]:
        rename = row[0]
        for i in range(3, 103+1):
            diff.append(
                int(row[i].replace(',','')) - \
                int(row[i+103].replace(',',''))
                )
        break

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False

plt.bar(range(101), diff)
plt.title(f'{rename}\n (남성인구)-(여성인구) 현황')

plt.ylabel('number')
plt.xlabel('age')
plt.show()