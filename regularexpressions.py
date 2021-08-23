#Example1

import  re

NameAge = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''

ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*', NameAge)

print(names)
print(ages)

ageDict = {}

x = 0

for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1

print(ageDict)

#Example2

import re

if re.search("inform", "we need to inform him with the latest information"):
    print("There is inform")

#Example3 Find a word in a string
import re

allinform = re.findall("inform","we need to inform him with the latest information")

for i in allinform:
    print(i)

#Example4 #Generate an iterator

import re

str  ="we need to inform him with the latest information"

for i in re.finditer("inform", str):
    loctup = i.span()
    print(loctup)

#Match words with particular pattren

import  re

str = "sat, hat, mat, pat"

allstr = re.findall("[shmp]at", str)

for i in allstr:
    print(i)


#Match series of range of charecters

import  re

str = "sat, hat, mat, pat"

allstr = re.findall("[h-m]at", str)

for i in allstr:
    print(i)


#Example

import  re

str = "sat, hat, mat, pat"

allstr = re.findall("[^h-m]at", str)

for i in allstr:
    print(i)


#Replace a string

import re

food = "hat rat mat pat"
regex = re.compile("[r]at")
food = regex.sub("food", food)
print(food)

#back slashes problem

import  re

str = "here is \\drogba"
print(re.search(r"\\drogba", str))

#match a single charecter

str = '''
keep the blue flag
flying high
chelsea
'''

print(str)

regex = re.compile("\n")
str = regex.sub(" ", str)
print(str)

#\b: backspace
#\f: formfeed
#\r: carriage return
#\v: vertical tab

#string matches

import  re

str = "12345"

print("Matches:", len(re.findall("\d", str)))

print("Matches:", len(re.findall("\d{5}", str)))

print("Matches:", len(re.findall("\D", str)))


#Example

import re
num  = "123 1234 12345 123456 1234567"
print("Matches:", len(re.findall("\d{5,7}", num)))

#Phone number

#\w [1-zA-Z0-9]
#\W[^a-zA-Z0-9]

phn = "412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}", phn):
    print("it is a phone number")


if re.search("\d{3}-\d{3}-\d{4}", phn):
    print("it is a phone number")

#\s [\f\n\t\v]
#\S [^\f\n\r\t\v]

if re.search("\w{2,20}\s\w{2,20}", "Praveen Reddy"):
    print("full name is valid")

#Email verification

import  re

email  = "sk@aol.com md@.com @seo.com dc@.com"

print("Email Maches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-za-z]{2,3}", email)))


#Example

import urllib.request

from re import  findall

url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"

responce = urllib.request.urlopen(url)

html = responce.read()

htmlstr = html.decode()

pdata = findall("\(\d{3}\) \d{3}-\d{4}", htmlstr)

for item in pdata:
    print(item)




