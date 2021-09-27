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
mx_result = []
mn_result = []

s_month = input('월:')
s_date = input('일:')

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == s_month and row[0].split('-')[2] == s_date:
            mx_result.append(float(row[-1]))
            mn_result.append(float(row[-2]))

# plt.rc('font', family ='Malgun Gothic')
plt.title('max & min temp ({}.{})'.format(s_month, s_date))
plt.plot(mx_result, 'hotpink')
plt.plot(mn_result, 'blue')
plt.show()