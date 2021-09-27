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

for row in data:
    if '제주' in row[0]:
        for i in row[2:3]:
            m.append(int(i.replace(',', '')))
        for i in row[105:106]:
            f.append(int(i.replace(',', '')))
            
        break

plt.rc('font', family='Malgun Gothic')
plt.title('제주특별자치도 남여 성비')

plt.pie([sum(m), sum(f)], labels=['남성', '여성'], autopct='%.1f%%',
        startangle=90)
plt.show()