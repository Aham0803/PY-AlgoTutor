# create few methods for deposit , withdraw and calculate interest.

class BankAccount:
    def __init__(self , account_number , account_holder , balance, interest_rate):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate

    def display_info(self):
        return f"Account Number : {self.account_number} , Account Holder:{self.account_holder} , Balance : {self.balance} , interest_rate : {self.interest_rate}"
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print (f"Deposited ${amount: .2f} . New Balance : ${self.balance : .2f}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance += amount
                print (f"Deposited ${amount: .2f} .New Balance : $ {self.balance : .2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdraw amount muust be positive.")

    def calculate_interest(self):
        interest = self.balance*(self.interest_rate/100)
        print(f"Interest for the current balance is : ${interest : 2f}")

bank_account = BankAccount("1234556" , "Gaurav" , 1000.00 , 5.0)
print(bank_account.display_info())
bank_account.deposit(500)
bank_account.withdraw(200)
bank_account.calculate_interest()