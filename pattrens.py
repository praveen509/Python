#pyramid
def pattern(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k -1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

pattern(10)

#Inverse pyramid

def pattern(n):
    k = 2 * n - 2
    for i in range(n,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

pattern(10)

#Right start pattren
def pattern(n):
    for i in range(0,n):
        for j in range(0,i + 1):
            print("* ", end="")
        print("\r")
    for i in range(n,-1,-1):
        for j in range(0,i + 1):
            print("* ",end="")
        print("\r")

pattern(5)

#Left start pattren

def pattren(n):
    k = 2 * n - 2
    for i in range(0, n-1):
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = - 1
    for i in range(n-1,-1,-1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

pattren(5)

#hourglass
def pattren(n):
    k = n - 2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = 2 * n - 2
    for i in range(0, n+1):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

pattren(5)

#half pyramid pattren
def pattren(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
pattren(5)

#left half pyramid pattren

def pattren(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
pattren(10)



#downward half pyramid
def pattren(n):
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

pattren(5)




#dimind pattren

def pattren(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for i in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = n - 2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

pattren(10)


#dimond star pattren

for i in range(5):
    for j in range(5):
        if i + j == 2 or i -j ==2 or i +j == 6 or j -i ==2:
            print("*", end="")
        else:
            print(end=" ")

    print()



#number pattrens

def pattern(n):
    x = 0
    for i in range(0,n):
        x = x + 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")

pattern(7)



#pascal's triangle pattern

def pattern(n):
    for i in range(0,n):
        for j in range(0, i + 1):
            print(function(i,j)," ", end="")
        print()
def function(n, k):
    res = 1
    if (k> n - k):
        k = n - k
    for i in range(0,k):
        res =  res * (n-i)
        res = res//(i+1)
    return res

pattern(5)


#half pyramid number pattren

def pattern(n):
    x = 0
    for i in range(0,n):
        x +=1
        for j in range(0,i+1):
            print(x, end=" ")
        print("\r")

pattern(10)

#Dymond shape
def pattren(n):
    k = 2 * n - 2
    x = 0
    for i in range(0,n):
        x = x + 1
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for i in range(0, i + 1):
            print(x, end=" ")
        print("\r")
    k = n - 2
    x = 0
    for i in range(n,-1,-1):
        x= x + 1
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(x , end=" ")
        print("\r")

pattren(7)


#Desending order pattern

def pattern(n):
    for i in range(n,0,-1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("\r")

pattern(5)


#Binary number pattern

def pattern(n):
    k = 2 * n -2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print('10', end="")
        print("\r")

pattern(5)


#right alphabetical triangle

def pattern(n):
    x = 65
    for i in range(0,n):
        ch = chr(x)
        x = x + 1
        for j in range(0,i+1):
            print(ch, end=" ")
        print("\r")

pattern(26)


#pyramid charectars

def pattern(n):
    k = 2 * n - 2
    x = 65
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            ch = chr(x)
            print(ch, end=" ")
            x +=1
        print("\r")

pattern(7)


#k shape charecter program
for i in range(7):
    for j in range(7):
        if j == 0 or i - j == 3 or i + j ==3:
            print("A", end="")
        else:
            print(end=" ")
    print()

#Trangle charecter
def pattern(n):
    k = 2 * n - 2
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x +=1
        for j in range(0, k):
            print(end=" ")
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")
pattern(5)

#Dymond char
def pattren(n):
    k = 2 * n - 2
    x = 65
    for i in range(0,n):
        ch  = chr(x)
        x = x + 1
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for i in range(0, i + 1):
            print(ch, end=" ")
        print("\r")
    k = n - 2
    x = 65
    for i in range(n,-1,-1):
        ch = chr(x)
        x= x + 1
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(ch , end=" ")
        print("\r")

pattren(25)






