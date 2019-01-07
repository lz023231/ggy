import  datetime
time1 = "2019-1-31"
time2 = "2019-2-28"
d1 = datetime.datetime.strptime(time1,'%Y-%m-%d')
d2 = datetime.datetime.strptime(time2,'%Y-%m-%d')
#m = d2 - d1
#t = m.days/30
t = round((d2 - d1).days/30)
print(t)
