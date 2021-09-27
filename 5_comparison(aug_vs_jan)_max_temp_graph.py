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
aug = []
jan = []

for row in data:
    month = row[0].split('-')[1]
    if row[-1] != '':
        if month =='08':
            aug.append(float(row[-1]))
        if month =='01':
            jan.append(float(row[-1]))
plt.title('Weather')
plt.hist(aug, bins=100, color='r')
plt.hist(jan, bins=100, color='b')
plt.show()