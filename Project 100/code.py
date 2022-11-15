class ATM:
    def __init__(self, balance, name, pin):
        self.balance = balance
        self.name = name
        self.pin = pin
    
    def checkBalance(self):
        p = int(input('What is your account pin?: '))
        if (p == self.pin):
            print(self.name, 'has a balance of', self.balance);
        else:
            print('Invalid account pin, try again.')
            
    def modifyPin(self):
        p = int(input('Verify that you own this account with a 4-digit pin: '))
        if (p == self.pin):
            self.pin = int(input('New pin: '))
        else:
            print('Invalid pin.')
            
    
customer1 = ATM(1000, 'Bob', 1234)
customer1.modifyPin()

customer1.checkBalance()
