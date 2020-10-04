s =input('enter input:')
output = ''
for x in s:
    if x.isalpha():
        ch = x
    else:
        d =int(x)
        output=output+ ch*d
print(output)




