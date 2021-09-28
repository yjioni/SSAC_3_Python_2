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
header = next(data)

# '2021년08월_남_100세 이상' 103
# '2021년08월_여_0세' 106

name = input('읍면동 >:')

m = []
f = []
for row in data:
    if name in row[0]:
        for i in range(3, 103+1):
            m.append(int(row[i].replace(',','')))
            f.append(int(row[i+103].replace(',','')))
            full_name = row[0]
        break



plt.rc('font', family='Malgun Gothic')
plt.title(f'{full_name}\n성별 연령별 인구 데이터')

plt.plot(m, label='Male')
plt.plot(f, label='Female')
plt.xlabel('age')
plt.ylabel('num')
plt.legend()

plt.show()