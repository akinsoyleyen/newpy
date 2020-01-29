print("How many cars do you own?")
num_cars = input()
try:
    if int(num_cars) > 2:
        print("You have alot of cars")
    elif int(num_cars) < 0:
        print("You cant have negative numbers mate!")
    else:
        print("That is not a lot of cars!")
except:
    print("You need to write a number!")