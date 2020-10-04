vowels = ['a','e','i','o','u']
word = input('enter the str:')
result =[]
for ch in word:
    if ch in vowels:
        if ch not in result:
            result.append(ch)
print(result)            
print('no of vowels',len(result))

vowels = ['a','e','i','o','u']
word = input('enter the str:')
result =[]
for ch in vowels:
    if ch in word:
        result.append(ch)
print(result)        
print('no of vowels',len(result))
