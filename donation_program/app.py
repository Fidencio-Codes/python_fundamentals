from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register 

database = {"admin": "password123"}
donations = []
authorized_user = ""

if authorized_user == "":
    print("\nYou must be logged in to donate.")
else:
    print(f"Logged in as: {authorized_user}")

while True: 
    show_homepage()
    option = input("Choose your option: \n")
    if option == "1":
        authorized_user
        username = input("What is your username? ")
        password = input("What is your password? ")
        authorized_user = login(database, username, password)
    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print(f"Logged in as {username}")

    if option == "2":
        username = input("Enter username? ")
        password = input("Enter password? ")
        authorized_user = register(database, username)
        # print(authorized_user)
        if authorized_user != "":
            database[username] = password
            # print(database)

    if option == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)

    if option == "4":
        show_donations(donations)

    if option == "5":
        print(f"Goodbye {username}")
        break
