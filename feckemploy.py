from random import *
alpha = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
cities = ['Chennai','Bangalore','Pune','Mumbai','Delhi']
designation = ['software engineer','senior software engineer','Team lead','Project lead']
def fack_name():
    name = choice(alpha).upper()
    n = randint(2,9)
    for x in range(n):
        name = name+choice(alpha)
    return name


def fack_eno():
    eno = 'e-'
    for x in range(4):
        eno = eno+choice(digits)
    return eno


def fack_salary():
    salary = uniform(10000,50000)
    return salary


def fack_city():
    city = choice(cities)
    return city


def fack_mobnum():
    num = str(randint(6,9))
    for x in range(9):
        num = num + choice(digits)
    return num


def fack_dsig():
    dsig = choice(designation)
    return dsig


    
def fack_data():
    print('EMPLOYE NAME:',fack_name())
    print('EMPLOYE NO  :',fack_eno())
    print('EMPLOYE SALARY :{:.2f}'.format(fack_salary()))
    print('EMPLOYE CITY   :',fack_city())
    print('EMPLOYE MOBILE NO  :',fack_mobnum())
    print('EMPLOYE DISIGNATION:',fack_dsig())
for x in range(10):
    
    fack_data()
    print()
    
    
    

