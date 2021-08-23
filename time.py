#Ex1
import  time
print(time.time())
print(time.ctime(1629529499.4345753))
print(time.localtime())
a = time.localtime()
print(time.mktime(a))
print(time.asctime(a))
print(time.strftime("%m/%d/%y"))
y = "08 August 2021"
print(time.strptime(y,"%d %B %Y"))