class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount.")
    
    def get_balance(self):
        return self.__balance  # Public method to access private attribute

# Create an instance of BankAccount
account = BankAccount("John", 1000)

# Accessing public methods
account.deposit(500)
account.withdraw(200)

# Accessing balance through a public method
print("Account Balance:", account.get_balance())

# Direct access to private attribute will result in an error
# print(account.__balance)  # Uncommenting this line will raise an AttributeError
