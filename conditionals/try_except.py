end_of_loop = False
while end_of_loop is False:
    try:
        x = int(input("Input an integer: "))
        print(x)
    except:
        print("Something went wrong! Try again. ")
        end_of_loop = False
    else: 
        print("Nothing went wrong")
        end_of_loop = True