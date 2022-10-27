def show_balance(balance):
    print("Current balance: $", balance)

def deposit(balance):
    amount = int(input("Enter amount to deposit: $"))
    return "New Balance: $", balance + amount

def withdraw(balance):
    amount = int(input(f"Enter amount to withdraw: $"))
    return "New Balance: $", balance - amount

def logout(name):
    print(f"Goodbye {name}")

