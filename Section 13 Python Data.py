# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:16:56 2020

@author: Hari
"""


s ={10,20,30}
s.clear()
print(s)

s = {10,20,30,40}
s.discard(30)
print(s)
s.discard(50)
print(s)



s = {10,20,40,30}
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)


#union metho
s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3=s1.union(s2)
print('union set:',s3)
s3 = s1|s2
print('union set:',s3)

#inersection( )method

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3=s1.intersection(s2)
print('intersection set:',s3)
s3 = s1&s2
print('intersection set:',s3)


#diffrence( )method
s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3=s1.difference(s2)
print('difference set:',s3)
s3 = s2-s1
print('difference set :',s3)

#symmitric_difference

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3=s1.symmetric_difference(s2)

print('sym_dif',s3)
s3 = s1^s2
print('sym_dif',s3)

#aliasing

s1 ={10,20,30}
s2 = s1
s3 = s1.copy()
s1.pop()

print(s2)
print(s1)
print(s3)


l = [10,10,20,30,20,10,30]
s = set(l)
print(s)
l1 = list(s)
print(l1)

l=[10,20,30,40,10,30,10,20,50]
l2 =[ ]
s1={l2.append(x)for x in l if x not in l2}
print(l2)


word = input('enter the word:')
s = set(word)
v ={'a','e','i','o','u'}
result = s&v
print(result)