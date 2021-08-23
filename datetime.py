import datetime
print(datetime.datetime(2019,6,7,4,30,54,678))
print(datetime.datetime.now())

v = datetime.datetime.now()
print(v.year)


b1 = datetime.timedelta(days=20)
b2 = datetime.timedelta(days=30)
b3 = b1-b2
print(b3)
print(type(b3))