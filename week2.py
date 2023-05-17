class CheckingAccount:
    def __init__(self,name,address,account_number,balance):
        self.name = name
        self.address = address
        self._account_number = account_number
        self._balance = balance
        
    def debit(self,amount):
        self._balance -= amount
        
    def credit(self, amount):
        self._balance += amount
        
    def get_balance(self):
        return self._balance
    
    
#Driver application
account = CheckingAccount("Romero Juan","244 N St","987654321",1000.00)
    
account.credit(500.00)
account.debit(200.00)
    
print("Account balance: ",account.get_balance())