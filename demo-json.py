import json

people_string='''
{
"people":[
{
"emp_name":"John parker",
"emp_no":"12334",
"emp_email":["jognparker@dummyemail.com"],
"has_license":"false"
},
{
"emp_name":"Harshit kant",
"emp_no.":"3445",
"emp_email":"null",
"has_licence":"true"
}
]
}
'''

data = json.loads(people_string)
print(data)
print(type(data))
print(type(data['people']))

for person in data['people']:
    print(person['emp_name'], person['emp_email'])