s = 'ABCABCABCA'
subs = input('enter the sub string:')
i = s.find(subs)
if i== -1:
    print('specified substring not found...')
while i!=-1:
    print('{} present at index {}'.format(subs,i))
    i = s.find(subs,i+len(subs),len(s))
print('total count of occurrences:',s.count(subs))    