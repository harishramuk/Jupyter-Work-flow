import json
employee = {'name':'harris',
            'age':29,
            'salary':50000,
            'is marrid': True,
            'is having car': None}

json_string = json.dumps(employee,indent = 4)
print(json_string)

with open('emp.json','w') as f:
    json.dump(employee,f,indent = 4)