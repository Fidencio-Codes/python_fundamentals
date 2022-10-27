# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

### MODULES ###
import random
import os 
import time

### ASCII ART ###
loser = "\n(⋟﹏⋞)"
angry_loser = "\n\n(╯°□°╯︵ ┻━┻ *flips table*"
winner = "\n\nWho's a winner? (☞ﾟ∀ﾟ)☞ You are! \n\nᕕ(⌐■_■)ᕗ ♪♬"
logo = "\nWelcome to ENRIQUE'S Number Guessing GAME!"

### FLAGS ###
end_of_game = True
gameplay = True

### FUNCTIONS ###

# Player chooses difficulty level
def difficulty():
    global life_amt
    mode = input("\nChoose a difficulty. \nType 'easy', 'medium', or 'hard' then hit ENTER: ").lower()
    if mode == 'easy': life_amt = 10
    elif mode == 'medium': life_amt = 7
    else: life_amt = 5
    print(f"\nYou have {life_amt} attempts left to guess the number.")

# Player guesses 
def playing():
    global guess
    try: guess = int(input("\nMake a guess: "))
    except TypeError: print("Not a number! Guess again")
    guesses_left()

# Computer checks guess, penalizes if incorrect 
def guesses_left():
    global gameplay, life_amt, random_number
    if guess < random_number:
        life_amt -= 1
        print("\nToo low.", "\nGuess again.", loser)
    elif guess > random_number:
        life_amt -= 1
        print("\nToo high.", "\nGuess again.", loser)
    print(f"\nYou have {life_amt} attempts left to guess the number.") 
    if life_amt > 0:
        playing()
    else life_amt < 0:
    

# Check if player lost, lives = 0
def check_lives():
    global gameplay, life_amt, end_of_game
    if life_amt == 0: 
        print("No more guesses left. YOU LOST.", angry_loser)
        gameplay = False
    check_won()

# Checks if player won, number guess
def check_won():
    global gameplay
    if guess == random_number:
        gameplay = False
        print(f"\nYou guessed the number correctly! {guess}", winner)

# Clears terminal screen 
def cls():
    global time_delay
    time_delay = time.sleep(3)
    print("\nHave a great day!") 
    os.system('cls' if os.name == 'nt' else 'clear')
    #nt for windows, running system call 'cls' else 'clear' for linux os. this way is more cross-platform       

### START of GAME ###
while end_of_game:
    global life_amt
    random_number = random.randint(1,100)
    print(logo)
    print("\nI'm thinking of a number between 1 and 100.")
    difficulty()

    ### GAMEPLAY ###
    while gameplay:
        playing()
        check_lives()

    end_of_game == False


### NOTES ###
# try - lets you test a block of code for errors.
# except - lets you handle the error.
# else - lets you execute code when there is no error.
# finally - lets you execute code, regardless of the result of the try- and except blocks.

        
