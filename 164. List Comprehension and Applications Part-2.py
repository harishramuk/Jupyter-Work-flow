l = [x for x in range (1,11)]
print (l)


l = [x*x for x in range (1,11)]
print (l)

l = [2**x for x in range (1,6)]
print (l)

l = [x for x in range (1,101) if x%10==0]
print (l)



l1 = [10,20,30,40]
l2=[40,30,60,70]
l = [x for x in l1 if x not in l2]
print (l)


l1 = [10,20,30,40]
l2=[40,30,60,70]
l = [x for x in l1 if x  in l2]
print (l)

l = ['HARISH','MAHE','VINOTH','PREM']
l2=[word[0]for word in l]
print(l2)

s = 'the quick brown fox jumps over the lazy dog'
words = s.split()
l =[[word.upper(),len(word)] for word in words]
print(l)