n = int(input('enter the number:'))
n1 = 2
while n1<=n:
    is_prime = True
    for i in range(2,n1):
        if n1%i==0:
            is_prime = False
            break
    if is_prime == True:
        print(n1)
    n1=n1+1
        
             