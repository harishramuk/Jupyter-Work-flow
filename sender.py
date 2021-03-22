from emp import Employee
import pickle
with open('emp.det','wb') as f:
    while True: # we want add multiple emp data so we use while loop.
        
        eNo =int(input('enter emp no:' ))
        eName = input('enter the emp name:')
        eSal = float(input('enter the sal:'))
        eAddr = input('enter the emp addr:')
    
        e = Employee(eNo,eName,eSal,eAddr) # we get dynamic type input,so we have to creat object 
        pickle.dump(e,f)  #that created object we have to send emp.det file 
        option = input('if you want add more employee [yes/no]:')
        if option.lower() =='no':
            break
print('all emp object serialization...')