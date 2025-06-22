class BankAccount():
    bank_name="MyBank"
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance="0"
    def display(self):
        print("Bank Name:",self.bank_name)
        print("Account_holder:",self.account_holder)
        print("balance:",self.balance)
        
ram=BankAccount("Ram","123")
ram.display()
