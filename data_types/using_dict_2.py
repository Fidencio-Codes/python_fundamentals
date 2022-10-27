# dictionaries are mutable data types
state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", 
                  "California": "Sacramento"
                  }

for states in state_capitals:
    print(states)

for city in state_capitals.values():
        print(city)
# uses .values() method to print out only the value 

for states in state_capitals:
    print(state_capitals[states], "is the capital of", states)

for states, city in state_capitals.items():
    print(city, "is the capital of", states)