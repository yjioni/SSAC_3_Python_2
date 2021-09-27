import csv
import matplotlib.pyplot as plt
import pandas as pd


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

for i in range(7):
    next(data)
header = next(data)

years = []
mx_temp = []
mn_temp = []

month = '{:02d}'.format(int(input('월 입력: ')))
date = '{:02d}'.format(int(input('날짜 입력: ')))


for row in data:
    # print(row)
    if len(row) != 0 and row[-1] != '':
        if row[0].split('-')[1] == month \
        and row[0].split('-')[2] == date:
            years.append(row[0].split('-')[0])
            mx_temp.append(float(row[-1]))
            mn_temp.append(float(row[-2]))

data = {'year':years, 'min_temp':mn_temp, 'max_temp':mx_temp}
df = pd.DataFrame(data)
df = df.set_index(['year'])

df.plot()
plt.title('({}/{}) min&max degree'.format(month, date))

plt.show()

f.close()
