#KEYS & VALUES

d = {100:'A',200:'B',300:'C'}
print(d.keys())

for key in d.keys():
    print(key)

print(d.values())
for valu in d.values():
    print(valu)
    


#item method
print(d.items())
for item in d.items():
    print(item) 
for k,v in d.items():
    print(k,'---------',v)    