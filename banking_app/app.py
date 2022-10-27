from banking_pkg import account

print("          === Automated Teller Machine ===          ")
name = (input("Enter name to register: "))
pin = input("Enter PIN: ")
balance = 0
print(f"{name} has been registered with a starting balance of ${balance}")

def atm_menu(name):
    print("          === Automated Teller Machine ===          ")
    print("")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

name_to_validate = ""
pin_to_validate = ""
while True:
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name == name_to_validate and pin == pin_to_validate:
        print("Login successful!")
        break
    else:
        print("Invalid credentials")

while True: 
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        account.deposit(balance)
    elif option == "3":
        account.withdraw(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid Option")
