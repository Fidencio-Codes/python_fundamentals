def login(database, username, password):
    global authorized_user
    if username in database and database[username] == password:
        print(f"\nWelcome back {username}!")
    elif username in database and database[username] != password:
        print("\nInvalid login, password does not match.")
        return ""
    else:
        print("\nUser not found. Please register.")
        return ""

def register(database, username):
    global authorized_user
    if username in database:
        print("\nUsername already registered.")
        return ""
    print("\nUsername",username,"registered.")
    return username
