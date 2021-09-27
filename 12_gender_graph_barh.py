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

data = csv.reader(f)

m = []
f = []
area = input('읍명동 단위 입력:')
for row in data:
    if area in row[0]:
        for i in range(0, 101):
            m.append(int(row[i+3]))
            f.append(int(row[-(i+1)]))            

f.reverse()

plt.rc('font', family='Malgun Gothic')
plt.title(f'{area} 성별 인구 수')
plt.barh(range(101), m)
plt.barh(range(101), f)
plt.show()
