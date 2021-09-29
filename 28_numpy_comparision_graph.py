import csv
import matplotlib.pyplot as plt
import numpy as np

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
print(header)
data = list(data)

name = input('읍면동 입력 >>>')
mn = 1
result_name =''
result = 0

for row in data:
    for i in range(1, 103+1):
        row[i] = row[i].replace(',','')
    if name in row[0]:
        home = np.array(row[3:], dtype=int)/int(row[2])
        name = row[0][:(row[0].index('('))]

for row in data:
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum((home-away)**2)
    if s < mn and name not in row[0]:
        mn = s

        result_name = row[0][:row[0].index('(')]
        result = away

plt.style.use('ggplot')
plt.figure(figsize=(5, 3), dpi=200)

plt.rc('font', family='Malgun Gothic')
plt.title(f'\'{name}\'지역과\n 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()


f.close()