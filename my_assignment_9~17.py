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

area = input('읍면동 입력>')

name = ''
m = []
f = []

for row in data:
    if area in row[0]:
        num = row[0].index('(')
        name = row[0][:num]
        for i in range(1, len(row)):
            row[i] = int(row[i].replace(',',''))
        for j in range(3, 103+1):
            m.append(row[j])
            f.append(row[j+103])
        break

minus_m = [m[k]*-1 for k in range(len(m))]

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False

ax1 = plt.subplot(2, 2, 1)
plt.plot(m, label='male', color='lightgreen')
plt.plot(f, label='female', color='tomato')
plt.title(f'{name}\n여성&남성 연령별 인구수')
plt.legend()
plt.xlabel('age')
plt.ylabel('number')


ax2 = plt.subplot(2, 2, 2)
plt.scatter(m, f, c=range(101), alpha=0.5, cmap='jet')
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'gray')
plt.xlabel('male')
plt.ylabel('female')
plt.title(f'{name}\n여성&남성 연령별 인구수')
 

ax3 = plt.subplot(2, 2, 3)
colors = ['darkseagreen', 'lightcoral']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
plt.pie([sum(m), sum(f)], labels=['남성', '여성'], autopct='%.1f%%',
        startangle=90, colors = colors, wedgeprops=wedgeprops)
plt.title(f'{name}\n여성&남성 성비')


ax4 = plt.subplot(2, 2, 4)
plt.barh(range(101), minus_m, label='male', color='lightgreen')
plt.barh(range(101), f, label='female', color='tomato')
plt.title(f'{name}\n여성&남성 연령별 인구수')
plt.xlabel('number')
plt.ylabel('age')
plt.legend()


plt.tight_layout()
plt.show()
