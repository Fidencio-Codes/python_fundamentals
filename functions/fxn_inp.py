# Function that allows for input

# def greet_name(name):
#     print(f"What's up {name}?")
#     print(f"How's it going, {name}?")
# greet_name("Fidencio")

# name is parameter, name of the data being 
    #passed through a function
    # inside def fxn 
# Fidencio is the argument, value of the data 
    # inside fxn call 

##################################################
# Positional Arguments, add as many arguments needed
# parameters are dependent on index location
    # so your arguments need to match the 
    # index of the parameter set
def greet_with(name, location, name_2):
    print(f"Hello, {name}.")
    print("Where are you?")
    print(f"I am in {location}!")
    print(f"This place is amazing, {name_2}.")
greet_with("Eunice","Berlin", "Larry")

# You can use keyword arguments to avoid positional issues 
def greet_with_key(name, location, name_2):
    print(f"Hello, {name}.")
    print("Where are you?")
    print(f"I am in {location}!")
    print(f"This place is amazing, {name_2}.")
greet_with_key(name ="Eunice", name_2 ="Larry", location ="Berlin")

# keyword arugments are legit useful, order does 
#    not matter 
# keep in mind it means more code written so use 
#   your judgment that this is needed 
