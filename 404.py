import json


with open('emp.json','r') as f:
    
    employee = json.load(f)
print(employee)
for k,v in employee.items():
    print(k,':',v)