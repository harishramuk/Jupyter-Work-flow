s1 = 'lazy'
s2 = 'zaly'
if sorted(s1)==sorted(s2):
    print('this two str is anagrams..')
else:
    print('this two str is not anagrams..')    
    
    
s = input('enter str: ')

if s==s[::-1]:
    print('this str is palindrome..')
else:
    print('this two str is not palindrome..')    
        