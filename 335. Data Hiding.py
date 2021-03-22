class account:
    def __init__(self,initial_balance):
        self.__balance = initial_balance
    def getbalance(self):
        print('enter the correct user name and password...')
        count = 0
        username = ''
        password = ''
        while username != 'harish' and password != 'harrishack' and count < 3:
            username = input('enter the user name:')
            password = input('enter the password:')
            
            if username == 'harish' and password == 'harrishack':
       
                return self.__balance
                
            else:
                print('access denied. try again...')
                
                count = count +1
        print('your cross your asses limit,plz try again some times..')
                
a = account(50000)
print(a.getbalance())
        