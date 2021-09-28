import csv
import matplotlib.pyplot as plt
import math


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

m = []
f = []
size = []

area = input('읍면동 입력 >>> ')

for row in data:
    if area in row[0]:
        for i in range(3, 104):
            m.append(int(row[i].replace(',', '')))
            f.append(int(row[(i+103)].replace(',','')))            
            size.append(math.sqrt(int(row[i].replace(',', '')) + int(row[i+103].replace(',',''))))
        break


# 마이너스 부호 깨짐 해결
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False

plt.figure(figsize=(4,3), dpi=250)
plt.title('{} 연령별 인구분포'.format(area))

plt.scatter(m, f, s=size, c=range(101), alpha=0.5, cmap='jet')
plt.colorbar()

plt.plot(range(max(m)), range(max(m)), 'g')

plt.xlabel('남성')
plt.ylabel('여성')

plt.show()
