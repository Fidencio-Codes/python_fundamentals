programming_dictionary = {
    "Bug": "An error in a program tha prevents it from running as intended.",
    "Function": "A piece of code that you can easily call over and over again",  
}

print(programming_dictionary["Function"])

# need to use correct data type when calling dictionary 

programming_dictionary["Loop"] = "The action of iterating something over and over"
# how to add items to your dictionary 
# print(programming_dictionary) tp check loop was added
 
empty_dictionary = {}

# wipe existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

for thing in programming_dictionary:
    print(thing)
# iterate each of the keys in the dictionary
# "thing" is the temporary variable assigned to iterate 
