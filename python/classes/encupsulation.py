class Bankaccount:
    
    def __init__(self, acc = 713625, bal = 500):
        self.acc = acc
        self.__bal = bal
        
    def credentials(self):
        name = input("Enter name: ")
        return f"Welcome {name}"
    
    def choose(self):
        user = input("choose what you want to do(Withdraw, Deposit,Balance): ").lower().strip()
        if user == "withdraw" or user == "w":
            return self.withdraw()
        elif user == "deposit" or user == "d":
            return self.deposit()
        elif user == "balance" or user == "b":
            return self.Balance()
        
    def deposit(self):
        try:
            amount = int(input("Enter amount: "))
            if amount > 0:
                self.__bal += amount
                return f"Amount deposited is: {amount}, Balance is {self.__bal}"
            elif amount < 0:
                return f"You cannot deposit {amount}"
            else:
                return "Invalid input"
        except ValueError:
            return "Invalid input!"
        
    def withdraw(self):
        try:
            amount = int(input("Enter amount: "))
            if amount > 0:
                self.__bal -= amount 
                return f"Amount withdrawn is: {amount}, Balance is:{self.__bal}"
            elif amount < 0:
                return f"You cannot withdraw {amount}"
            else:
                return "Invalid input"
        except ValueError:
            return "Invalid input!"
        
    def balance(self,pin = 4444):
        try:
            ent_pin = int(input("Enter pin: "))
            if ent_pin == pin:
                return f"Account number{self.acc}: Balance: {self.__bal}"
            else:
                return "Wrong pin!"
        except ValueError:
            return "Invalid Input!"
        
bank = Bankaccount()
print(bank.credentials())
print(bank.choose())
