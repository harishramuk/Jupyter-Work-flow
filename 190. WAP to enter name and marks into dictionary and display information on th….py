n = int(input('enter the number of student :'))
d = {}
for x in range (n):
    name = input('enter the student name:')
    mark = int(input('enter the stud mark:'))
    d[name]=mark
print('*'*30)
print('NAME','\t\t','MARK') 
print('*'*30)
for name in d:
    print(name,"\t\t",d[name])
