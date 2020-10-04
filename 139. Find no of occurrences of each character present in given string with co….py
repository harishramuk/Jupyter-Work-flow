s = 'AACCDDBBBAAC'
l = []
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print('{} occure {} times'.format(ch,s.count(ch)))



s = 'AACCDDBBBAAC'
s1=set(s)
for ch in sorted(s1):
    print('{} occure {} times'.format(ch,s.count(ch)))         