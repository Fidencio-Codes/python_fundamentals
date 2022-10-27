# dictionaries are mutable data types
# state_capitals = {"Washington": "Olympia", 
#                 "Oregon":"Salem", "California":"Sacramento"}
# print(len(state_capitals))a

# print(state_capitals["Washington"])
# print(state_capitals["Oregon"])
# print(state_capitals["California"])
# state_capitals["Washington"] = "Aberdeen" #to change value of key
# state_capitals["New York"] = "NYC" #to add another key-value pair
# print(state_capitals)

# del state_capitals["California"]
# print(state_capitals)

# remove_capital = state_capitals.pop("Oregon")
# print(state_capitals)

# del vs pop
# methods can return values with pop(), return value saved 
        # or assigned to variable to save like above 
# del straight up deletes entirely

popcorn_prices = {"small": 1.5, "medium": 4, "large": 5, "small": 1.5}
for size in popcorn_prices.keys():
        print(size)
for price in popcorn_prices.values():
        print(price)
for size, price in popcorn_prices.items():
        print(size, price)

# for duplicates, the last duplicate overrides the first one
print(popcorn_prices) 