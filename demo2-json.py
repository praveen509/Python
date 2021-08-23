import json

people_string='''
{
"people":[
{
"emp_name":"John parker",
"emp_no.":"12334",
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

data  = json.loads(people_string)
for person in data['people']:
    del person['emp_no.']

new_string = json.dumps(data, indent=2,sort_keys=True)
print(new_string)
