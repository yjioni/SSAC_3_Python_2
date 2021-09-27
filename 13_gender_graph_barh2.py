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
    if '신도림' in row[0]:
        for i in range(0, 101):
            m.append(-int(row[i+3]))
            f.append(int(row[-(i+1)]))            
f.reverse()

# 마이너스 부호 깨짐 해결
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False

plt.title('신도림동 연령별 남녀 성별 인구 분포')


plt.barh(range(101), m, label='male')
plt.barh(range(101), f, label='female')

# 범례
plt.legend()

plt.show()