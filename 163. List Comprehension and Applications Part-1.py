l =[10,20,[30,40]]
print(l[0])
print(l[1])
print(l[2])
print(l[2][0])
print(l[2][1])


l = [[10,20,30],[40,50,60],[70,80,90]]
print(l)

print('elements print row by row')
for x in l:
    print(x)
    
print('element print matrix style ')
for x in l:
    for y in x:
        print(y,end=' ')
    print()    