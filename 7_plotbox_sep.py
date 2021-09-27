import csv
import matplotlib.pyplot as plt

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
next(data)

month =[]
for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '09':
            month.append(float(row[-1]))

plt.boxplot(month)
plt.show()