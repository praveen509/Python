fruits = ['mango', 'grapes', 'ápple']

for fruit in fruits:
    print("Current fruit:", fruit)

print("Good Bye")

#-------------------------------------------------

fruits = ['mango', 'grapes', 'ápple']

for fruit in fruits:
    print("Current fruit:", fruit)

print("Good Bye")

#-------------------------------------------------

num = int(input("Number:"))
factorial = 1
if num < 0:
    print("must be positive")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1,num + 1):
     factorial = factorial * i

print(factorial)