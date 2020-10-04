# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:28:00 2020

@author: Hari
"""


number_of_student = int(input('enter the number of student:'))
d={}
for x in range(number_of_student):
    name = input('Enter the name of the student: ').upper()
    marks = int(input('Enter the student marks: '))
    d[name]=marks
print('student Data insertion completed...')
print('*'*30)
print('NAME',"\t\t",'MARKS')
print('*'*30)
for k,v in d.items():
    print(k,"\t\t",v)
print('Serching operation is starte,....')
while True:
    name =input('Enter the student name: ').upper()
    marks=d.get(name,-1)
    if marks == -1:
        print('the student name is not found,...')
    else:
        print('The student name is',name,'his marks',marks)
    countinu=input('if you know another student marks [Yes|No]: ')
    if countinu.lower()== 'no':
        break
print('thanks for using this app,.....')    