def show_homepage(): 
    print("         === DonateMe Homepage ===        ")
    print("------------------------------------------")
    print("| 1.    Login       | 2.  Register       |")
    print("------------------------------------------")
    print("| 3.    Donate      | 4.  Show Donations |")
    print("------------------------------------------")
    print("|                5.  Exit                |")

def donate(username):
    donation_amt = input("Enter amount to donate: $")
    donation_string = (f"{username} donated ${donation_amt}")
    print("Thank you for your contribution!")
    return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for amt in donations: 
            print(amt)

