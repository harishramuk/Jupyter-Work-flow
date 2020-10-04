l = [0,1,2,3,4,5,6,7,8,9]
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
l1=[]
for x in l:
    if iseven(x) == True:
        l1.append(x )
print(l1)        


l2 = list(filter(lambda n: n%2==0,l))
print(l2)
l3 = list(filter(lambda n: n%2!=0,l))
print(l3)


heroines = ['Katrina','Anuska','Thamana','Jothika','Kareena']
output = list(filter(lambda name: name[0]=='K',heroines))
print(output)
