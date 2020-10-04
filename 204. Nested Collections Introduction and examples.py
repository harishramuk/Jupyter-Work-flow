l = [(10,20,30),(40,50,60)]
print(l[0][2])
print(l[0][1])
print(l[1][2])
print(l[1][1])

d = { "cars":('Honda','MGM','Kivi'),
     "Mobiles":('samsung','Iphone','Nokia')}
print(d.get('cars')[0])
print(d["cars"][1])
print(d["cars"][2])
print(d["Mobiles"][2])
print(d["Mobiles"][1])
print(d.get('Mobiles')[0])

print(d['Mobiles'])

for x in d.get('cars'):
    print(x)
for x in d['Mobiles'] :
    print(x)
    