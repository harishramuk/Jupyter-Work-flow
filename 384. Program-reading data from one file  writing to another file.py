f1 = open('mobno.txt','r')
f2 = open('output.txt','a')
data = f1.read()
da=f2.write(data)
print(da)
f1.close()
f2.close()
print ('operation secces')
