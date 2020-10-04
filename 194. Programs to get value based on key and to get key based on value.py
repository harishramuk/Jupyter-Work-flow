# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:42:16 2020

@author: Hari
"""


d = {100:'a',200:'b',300:'a',400:'c'}
value = input('enter the value:')
avalable = False
for k,v in d.items():
    if v==value:
        print(v,'crospoinding key is:',k)
        avalable= True
if avalable == False:      
        
    print('the crospoinding value is not spisified')        