n = int(input('enter the prime number:'))
if n<=1:
    print('it is not prime number...')
    
else:
    is_prime=True
    for i in range (2,n//2+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print('it is prime number..')
        
    else:
        print('it is not prime number..')
    