
#  Nesting a list in the dictionary, value can only be one item. why not make it a list? 
# travel_log = {
#     "France": ["Paris", "Orleans", "Versailles"],
#     "El Salvador": ["San Salvador", "Santa Elena", "Berlin"],
#     "California": ["Sacramento", "Oakland", "Santa Ana"],
#     "Germany": ["Berlin", "Hamburg", "Potsdam"],
# }

# nesting dictionary in a dictionary
    # "France": {"cities_visited":["Paris", "Orleans" "Versailles"], "total_visited": 12},
    # "El Salvador": {"cities_visited":["San Salvador", "Santa Elena", "Berlin"], "total_visited": 12},
    # "California": {"cities_visited":["Sacramento", "Oakland", "Santa Ana"], "total_visited": 12},
    # "Germany": {"cities_visited": ["Berlin", "Hamburg", "Potsdam"], "total_visited": 12},

# for x in travel_log:
#     print(x)
# # print all key names in dictionary

# for x in travel_log:
#     print(travel_log[x])
# # print all values in dictionary

# for y in travel_log.values():
#     print(y)
# # return values of a dictionary

# for x in travel_log.keys():
#     print(x)
# # return key values of dictionary

# for x, y in travel_log.items():
#     if x == "France":
# loop through keys and values using item() method

# Nesting dictionary in a list
travel_log = [ 
    {
        "country" : "France", 
        "cities":["Paris", "Orleans", "Versailles"], 
        "visits": 3
    },
    {
        "country" :"El Salvador", 
        "cities":["San Salvador", "Santa Elena", "Berlin"], 
        "visits": 12
    },
    {   "country" :"California", 
        "cities": ["Sacramento", "Oakland", "Santa Ana"], 
        "visits": 8
    },
    {   "country" :"Germany", 
        "cities": ["Berlin", "Hamburg", "Potsdam"], 
        "visits": 4
    },
]

def add_new_country(country_visited, cities_visited, times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"] = cities_visited
    new_country["visits"] = times_visited
    travel_log.append(new_country)

def highest_visits():
    visit_list = []
    

add_new_country("Russia", ["Moscow", "Saint Petersburg", "Novosibirsk"], 2)
add_new_country("Spain", ["Barcelona", "Gybraltar", "Granada"], 7)
print(travel_log)   