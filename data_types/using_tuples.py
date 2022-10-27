my_tuple = (1,2,3,4,5)
print(my_tuple[0] + my_tuple[1])
print(my_tuple[-1] + my_tuple[-2])

total = 0
for n in my_tuple:
    total += n 
print(total)

# tuples are immutable(cannot modify)
# you can reassign the tuple variable tho

# tuples need  trailing comma
    # paranthesis is option
    # good practice to still use 
# example of what is not a tuple
    # tuple1 = ("Delta") 
    # not a tuple cuz it needs a comma
    # tuple1 = ("Delta",) is a tuple
