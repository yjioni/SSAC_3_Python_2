import csv
import matplotlib.pyplot as plt

f = open('C:/Users/oing9/Downloads/t-money.csv')
data = csv.reader(f)
header = next(data)

label = ['유임승차', '유임하차', '무임승차', '무임하차']

# 마이너스 부호 깨짐 해결
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False


for row in data:
    for i in range(4,8):
        row[i] = int(row[i].replace(',',''))
    
    color = ['darkorange', 'orange', 'gold', 'lightyellow']
    explode = [0.01, 0, 0, 0]
    wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 3}
    plt.pie(row[4:8], labels=label, autopct='%.1f%%', 
    startangle=90, colors=color, counterclock=False,
    explode=explode, wedgeprops=wedgeprops)
    plt.title(f'{row[3]}_{row[1]}')
    
    plt.axis('equal')

    plt.show()