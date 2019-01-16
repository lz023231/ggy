
import  datetime
import time
'''
time1 = "2019-1-31"
time2 = "2019-2-28"
d1 = datetime.datetime.strptime(time1,'%Y-%m-%d')
d2 = datetime.datetime.strptime(time2,'%Y-%m-%d')
#m = d2 - d1
#t = m.days/30
t = round((d2 - d1).days/30)
print(t)

t = "ceshi"
x = "ceshi01"
z = t+'01'

if x == t + "01":
    print('3')
else:
    print('ksdhf')
    
t = datetime.datetime.now().strftime('%Y-%m-%d')
y = t.split('-')
print(y)
h = '{}{}{}'.format('ceshi',y[1],y[2])
print(h)

print(t)
'''
t = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
print(t)