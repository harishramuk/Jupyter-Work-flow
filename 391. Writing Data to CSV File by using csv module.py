import csv
with open('emp.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['E-NO','E-NAME','E-SAL','E-ADDR'])
    while True:
        eno= int(input('enter the eno:'))
        ename = input('enter the ename:')
        esal = float(input('enter the esal:'))
        eaddr = input('enter the addr:')
        w.writerow([eno,ename,esal,eaddr])
        option = input('if you want add more detile [yes/No]:')
        if option.lower() =='no':
            break
print('your data added sucessfully...')