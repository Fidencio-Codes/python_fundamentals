# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# avg_height = 0
# for student in student_heights:
#     avg_height += 1
# avg_height = round(total_height/avg_height)
# print(avg_height)

# student_scores = input("Input a list of student scores 0-100: ")
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")

# Range function
# total = 0
# for number in range(2, 101, 2):
#     total = total + number
#     print(total)

# FizzBuzz exercise
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print(str(number) + "FizzBuzz")
#     elif number%3 == 0:
#         print(str(number) + "Fizz")
#     elif number%5 == 0:
#         print(str(number) + "Buzz")
#     else:
#         print(number)

# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw_list = []

for char in range(1, nr_letters +1):
    pw_list += random.choice(letters)
for char in range(1, nr_symbols +1):
    pw_list += random.choice(symbols)
for char in range(1, nr_numbers +1):
    pw_list += random.choice(numbers)

print(pw_list)
random.shuffle(pw_list)
print(pw_list)
final_pw = "".join(pw_list)
print(f"Your Password is: {final_pw}")   

# pw_letter = ""
# pw_symbol = ""
# pw_number = ""
# password_1 = ""
# total_num = 0

# for letter in range(0,nr_letters):
#     randnum = random.randint(0,51)
#     pw_letter += letters[randnum]
# total_num += nr_letters

# for sym in range(0,nr_symbols):
#     randnum = random.randint(0,8)
#     pw_symbol += symbols[randnum]
# total_num += nr_symbols

# for num in range(0,nr_numbers):
#     randnum = random.randint(0,9)
#     pw_number += numbers[randnum]
# total_num += nr_numbers

# password_1 = pw_letter + pw_symbol + pw_number
# password_2 = list(password_1)
# random.shuffle(password_2)
# final_pw = "".join(password_2)
# print(f"Your Password is: {final_pw}")