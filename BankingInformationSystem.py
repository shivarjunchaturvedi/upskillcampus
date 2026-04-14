class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance):
        self.accounts[name] = balance
        print("Account created successfully!")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            print("Amount deposited!")
        else:
            print("Account not found!")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                print("Withdrawal successful!")
            else:
                print("Insufficient balance!")
        else:
            print("Account not found!")

    def check_balance(self, name):
        if name in self.accounts:
            print(f"Balance: {self.accounts[name]}")
        else:
            print("Account not found!")


bank = Bank()

while True:
    print("\n1.Create Account\n2.Deposit\n3.Withdraw\n4.Check Balance\n5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        balance = int(input("Enter initial balance: "))
        bank.create_account(name, balance)

    elif choice == 2:
        name = input("Enter name: ")
        amount = int(input("Enter amount: "))
        bank.deposit(name, amount)

    elif choice == 3:
        name = input("Enter name: ")
        amount = int(input("Enter amount: "))
        bank.withdraw(name, amount)

    elif choice == 4:
        name = input("Enter name: ")
        bank.check_balance(name)

    elif choice == 5:
        break