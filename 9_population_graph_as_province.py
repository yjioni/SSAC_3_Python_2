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

result = []
area = input('읍면동 단위 입력:')

for row in data:
    if area in row[0]:
        for i in row[3:]:
            i = i.replace(',', '')
            result.append(int(i))
print(result)

plt.rc('font', family='Malgun Gothic')
plt.title('{} 연령별 인구 수'.format(area))         
plt.style.use('ggplot')
plt.plot(result)
plt.show()