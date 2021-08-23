count = 0

while count < 9:
    print('Number:', count)
    count = count+1

print('Good Bye')

#----------------------------------------

import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("sorry that you're giving up!")
        break
else:
    print("Çongratulation. You made it!")
