import json
from empobject406 import Employee

with open ('empobj406.json','w') as f:
    while True: # we want add multiple emp data so we use while loop.
        
        eno =int(input('enter emp no:' ))
        ename = input('enter the emp name:')
        esal = float(input('enter the sal:'))
        eaddr = input('enter the emp addr:')
    
        e = Employee(eno,ename,esal,eaddr)

        e_dict= e.__dict__
        json_str = json.dump(e_dict,f,indent=4)
        option = input('if you want add more employee [yes/no]:')
        if option.lower() =='no':
            break

with open('empobj406.json','r') as f:
    e_py_dict = json.load(f)


e = Employee(e_py_dict['eno'],e_py_dict['ename'],
             e_py_dict['esal'],e_py_dict['eaddr'])

e.display()