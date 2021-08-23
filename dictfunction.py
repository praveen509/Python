mydict = {'name':'praveen','place':'nellore'}
print(mydict)

mydict1 = dict(name='praveen',place='nellore')
print(mydict1)

#nested dictionaries

emp_details = {'Employee':{'Dave':{'ID':'001','salary':'2000','Designation':'Team Lead'},
                           'Praveen':{'ID':'002','salary':'4000','Designation':'Team Maganer'}}}

print(emp_details)

#Accessing Items
print(mydict['name'])
print(mydict.keys())
print(mydict.values())
print(mydict.get('name'))
for x in mydict:
    print(x)
for x in mydict.values():
    print(x)
for x,y in mydict.items():
    print(x,y)

#Updating Items
mydict['name'] = "Reddy"
mydict['age'] = '26'
print(mydict)

#Deleting Items
mydict.pop('name')
print(mydict)
mydict.popitem() #Removes the last item of the dictionary
print(mydict)
del mydict['place']
print(mydict)

#Dictionary to a Dataframe
emp_details = {'Employee':{'Dave':{'ID':'001','salary':'2000','Designation':'Team Lead'},
                           'Praveen':{'ID':'002','salary':'4000','Designation':'Team Maganer'}}}

import pandas as pd
df = pd.DataFrame(emp_details['Employee'])
print(df)