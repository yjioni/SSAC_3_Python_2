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
print(header)

# 데이터 정제

## 전체 역사 유/무임 승차/하차 구분자
## 승차
ttl_in_paid = 0
ttl_in_unpaid = 0
## 하차
ttl_out_paid =0
ttl_out_unpaid = 0

# 전체 이용현황 변수
names = []
stations = []
# 최다 이용 역사
mx = 0
mx_name = ''
mx_stations = []

for row in data:
    # 쉼표 구분 제거, 정수형으로 변경
    for i in range(4,8):
        row[i] = int(row[i].replace(',',''))
    
    ttl_in_paid += row[4]
    ttl_in_unpaid += row[6]
    ttl_out_paid += row[5]
    ttl_out_unpaid += row[7]
    
    names.append(f'({row[1]}){row[3]}')
    stations.append(row[4:7+1])

    # 최다 승하차 역
    num = row[4]+row[5]+row[6]+row[7]
    if num > mx:
        mx = num
        mx_name = f'({row[1]}){row[3]}'
        mx_stations = row[4:7+1]

print(mx_stations)

# 마이너스 부호 깨짐 해결
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False

explode = [0.02, 0]
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 2}

# 유임/무임승차 파이차트
plt.subplot(2, 2, 1)
plt.title('서울 지하철 유/무임 승차 비율')
plt.pie([ttl_in_paid, ttl_in_unpaid], labels=['유임승차', '무임승차'],
 autopct='%.1f%%', startangle=90, colors=['darkorange', 'gold'],
 counterclock=False, explode=explode, wedgeprops=wedgeprops)

# 유임/무임하차 파이차트
plt.subplot(2, 2, 2)
plt.title('서울 지하철 유/무임 하차 비율')
plt.pie([ttl_out_paid, ttl_out_unpaid], labels=['유임하차', '무임하차'],
 autopct='%.1f%%', startangle=90, colors=['orange', 'gold'],
 counterclock=False, explode=explode, wedgeprops=wedgeprops)

# 전체 이용객수 vs 최다 이용객 역 .. bar chart
ax1 = plt.subplot(2, 2, 3)
x = ['유임승차', '유임하차', '무임승차', '무임하차']

ax1.bar(x,
 [ttl_in_paid/10000, ttl_out_paid/10000, ttl_in_unpaid/10000, ttl_out_unpaid/10000],
 color=['darkorange', 'orange', 'gold', 'yellow'], label='서울 지하철 전체')
ax1.legend(loc=(0.6, 0.9))
ax1.set_ylabel('(만 명)')

ax2 = ax1.twinx()
ax2.plot(x, [ i/1000 for i in mx_stations], 'r*', label=f'{mx_name}역')
ax2.legend(loc=(0.6, 0.8))
ax2.set_ylabel(f'{mx_name} (천 명)')
plt.title(f'전체 vs {mx_name}역')

# 최다 이용객 역 유/무임 이용 파이차트
plt.subplot(2, 2, 4)
label = ['유임승차', '유임하차', '무임승차', '무임하차']
plt.title(f'\'{mx_name}\' 이용객 현황')
plt.pie(mx_stations, labels=label, autopct='%.1f%%', startangle=180, 
colors=['darkorange', 'orange', 'gold', 'yellow'],
counterclock=True, explode=[0.02,0,0,0], wedgeprops=wedgeprops)

plt.show()

data.close()