#Raise exception
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

#Assertion exception
import sys
assert ('linux' in sys.platform), "This code runs on linux only."

#Try and except block

def linux_interaction():
    assert ('linux' in sys.platform), "The function can only run on linux systems."
    print('Doing somethig')

try:
    linux_interaction()
except:
    print("Linux function was not executed")


#Try and except block

def linux_interaction():
    assert ('linux' in sys.platform), "The Function can only run on linux systems."
    print('Doing somethig')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("The linux_function() was not executed")

#Example

try:
    with open('file.log') as file:
        read_date = file.read()
except:
    print('could not open file.log')

#Example

try:
    with open('file.log') as file:
        read_date = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)


#Example

def linux_interaction():
    assert ('linux' in sys.platform), "The Function can only run on linux systems."
    print('Doing somethig')

try:
    linux_interaction()
    with open('file.log') as file:
        read_date = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('Linux linux_interaction() function was not executed')

#Example try, except and else

def linux_interaction():
    assert ('linux' in sys.platform), "The Function can only run on linux systems."
    print('Doing somethig')

try:
    print("try block passed")
except AssertionError as error:
    print(error)
else:
    print("Executing the else clause")

#Example try, except and else (you can also try to run code inside the else clause ans catch possible exceptions there as well)

def linux_interaction():
    assert ('linux' in sys.platform), "The Function can only run on linux systems."
    print('Doing somethig')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_date = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)

#try,except,else and finally

def linux_interaction():
    assert ('linux' in sys.platform), "The Function can only run on linux systems."
    print('Doing somethig')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_date = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("cleaning up, irrespective of any exceptions.")