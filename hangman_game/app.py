import random
import os
from game_pkg.ascii import logo, stages, sore_loser, winner
from game_pkg.wordset import word_set

## FUNCTION ##
def cls():
    os.system('cls' if os.name == 'nt' else 'clear') 

play_again = True
while play_again:
    print(logo)
    print("NOTE: You have 6 tries to guess all letters in the word")
    chosen_word = random.choice(word_set)
    lives_left = 6
    end_of_game = False

    #Testing code, run with code to know the answer
    print(f'Psst, the solution is {chosen_word}.\n')

    # Will show the spaces of every letter as underscores
    display = []
    for letter in chosen_word:
        display.append("_")

    # While not False
    while not end_of_game:
        # Check guessed letter
        guess = input("Guess a letter: ").lower()
        
        
        
        # Replaces underscore in display if letter is guessed 
        for index, value in enumerate(chosen_word):
            if value == guess:
                display[index] = guess 
        print(f"{' '.join(display)}")

        # Checks if your lives equals 0, this you lose
        if guess not in chosen_word:
            lives_left -= 1
            print(f"\nYou guessed {guess}, that's not in the word. You lost a life")
            if lives_left == 0:
                end_of_game = True
                print("\nYou lose!", sore_loser)
        
        # If you run out of underscores, that means you solved the word and WIN
        if not "_" in display:
            end_of_game = True
            print(winner)

        # prints the stage you're on based on how many lives you have
        print(stages[lives_left])

    # Looping game if you want to play again, or clearing terminal if you are done.
    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        cls()
    else: 
        cls()
        print("Thanks for playing!")
        play_again == False
        break