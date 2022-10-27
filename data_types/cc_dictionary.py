inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches = total_inches + inches
        print(total_inches)
        print("Total snowfall inches:", )
        return 0

print_total_snowfall(inches_snow) 

inches_snow["Thursday"] = int(input("How many inches did it snow Thursday? "))
print(inches_snow)
print_total_snowfall(inches_snow) 

