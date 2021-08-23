#File handling

import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'w')
file.close()

# Print file

import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'r')
print(file.read())
file.close()

#Read charecter 5
import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'r')
print(file.read(5))
file.close()

#Line by line output

import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'r')
print(file.readline())
file.close()

#Read third line only

import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'r')
print(file.readline(3))
file.close()

#Read line seperately

import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'r')
print(file.readlines())
file.close()

#For loop over a file object

import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'r')
for line in file:
    print(file.readlines())
file.close()


#Writing to an existing file

import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'w')
file.write("Hello World")
file.write("Hello World Again")
file.close()

#File overwriten

import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'w')
file.write("oops overwritten")
file.close()

#Appending
import os
file = open("C:/Users/pa108968/Desktop/test.txt", 'w')
file.write("oops overwritten")
file.write("appended")
file.close()

#Create new file
import os
file = open("C:/Users/pa108968/Desktop/test1.txt", 'x')
file.write("New file - edureka")
file.close()


#Deleting a file file
import os
if os.path.exists("C:/Users/pa108968/Desktop"):
    os.remove("C:/Users/pa108968/Desktop/test1.txt")
else:
    print("The file does not exist")


#Deleting a folder
import os
if os.path.exists("C:/Users/pa108968/Desktop"):
    os.rmdir("C:/Users/pa108968/Desktop/Test")
else:
    print("The folder does not exist")











