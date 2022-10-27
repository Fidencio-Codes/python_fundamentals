# empty_set = set()

# computer does not remember order of set, printing abcd 
    # below will rearrange the order of the set because of this 
    # set items are not indexed, like a list 
# sets are mutable, cannot contain list, dictionaries, set

# unordered callection of values, comma separated 
    # cache in memory will save number values and will be ordered 
    # strings and other data types are unordered in any case  
    # depends on the algorithms in each application/website etc

# numbers_set = {1,2,3,4,(5,6),4}
# print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}
# abcd = ""
# for word in words_set:
#     abcd += word
# print(abcd)
#############################################
# if "Alpha" in words_set:
#     print("Alpha is in set")
# else:
#     print("Alpha is not in set")

words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)