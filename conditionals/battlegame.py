wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_dmg = 150
elf_dmg = 100
human_dmg = 20

dragon_hp = 300
dragon_dmg = 50

print("Wizard")
print("Elf")
print("Human")
character = input("Choose your character: ")

while True:
    if character == "Wizard":
        my_hp = wizard_hp
        my_dmg = wizard_dmg
        print("You have chosen: " + character)
        print(f"Health: {my_hp}")
        print(f"Damage: {my_dmg}")
        break
    elif character == "Elf":
        my_hp = elf_hp
        my_dmg = elf_dmg
        print("You have chosen: " + character)
        print(f"Health: {my_hp}")
        print(f"Damage: {my_dmg}")
        break
    elif character == "Human":
        my_hp = human_hp
        my_dmg = human_dmg
        print("You have chosen: " + character)
        print(f"Health: {my_hp}")
        print(f"Damage: {my_dmg}")
        break
    else:
        print("Unknown Character. Try again")
        break

while True: 
    dragon_hp -= my_dmg
    if dragon_hp > 0:
        print(f'The {character} damaged the dragon!')
        print(f"Dragon's hitpoints are now {dragon_hp}")
    elif dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_dmg
    if my_hp > 0:
        print(f'The Dragon strikes back at {character}')
        print(f'The {character} hitpoints are now {my_hp}')
    elif my_hp <= 0:
        print(f'The {character} lost the battle!')
        break