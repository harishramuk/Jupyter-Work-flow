class customer:
    '''Customer class developed dy harrish for bank operation'''
    bank_name = 'City Bank'
    def __init__ (self,name,balance = 0.0):
        self.name = name
        self.balance = balance
    def Deposit(self,amount):
        self.balance = self.balance + amount
        print('Balance after deposit:',self.balance)
    def Withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient fund..cannot perform this...')
        else:
            self.balance = self.balance - amount
            print('Balance after withdraw:',self.balance)
        
        
print('welcome to ',customer.bank_name)
name = input('Enter the name:')
c = customer(name)
while True:
    print('d - deposit, w - withdraw, e - exit:')
    
    option = input('enter the option..')
    if option.lower() == 'd':
        amount = float(input('enter the deposit amount:'))
        c.Deposit(amount)
    elif option.lower() =='w':
        amount = float(input('enter the withdraw amount:'))
        c.Withdraw(amount)
    elif option.lower() == 'e':
        print('Thanks for using our bank...')
        break
    else:
        print('Ivalide option plz... chose valide option...')
