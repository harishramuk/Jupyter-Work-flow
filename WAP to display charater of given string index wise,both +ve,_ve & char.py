#WAP to display charater of given string index wise,both +ve,_ve & char

s = input('enter the string:')
i = 0
for x in s:
    print('the chareter present of +ve index:{} and -ve index:{} is char:{}'.format(i,i-len(s),x))
    i=i+1