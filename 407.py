import jsonpickle
from empobject406 import Employee

with open ('empobj407.json','w') as f:
    while True: # we want add multiple emp data so we use while loop.
        
        eno =int(input('enter emp no:' ))
        ename = input('enter the emp name:')
        esal = float(input('enter the sal:'))
        eaddr = input('enter the emp addr:')
    
        e = Employee(eno,ename,esal,eaddr)

        json_string = jsonpickle.encode(e)#
        
        f.write(json_string)
        
        e2 = jsonpickle.decode(json_string)
                              
        option = input('if you want add mor detils [yes/no]:')
        if option.lower() =='no':
            break
e2.display()        
