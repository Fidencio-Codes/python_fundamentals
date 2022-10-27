import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choose = input("Press enter to pick a card, or Q then enter to quit: ")
    if choose == "Q":
        print("Goodbye.")
        break
    else:
        choose = random.choice(diamonds)
        hand.append(choose)
        diamonds.remove(choose)
        print("Remaining cards: ", diamonds)
        print("Your hand: ", hand)
if not diamonds:
    print("There are no more cards")