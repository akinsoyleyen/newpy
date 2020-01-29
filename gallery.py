from sys import exit

cash = 100000
ferrari_cost = 50000
lambo_cost = 60000

def ferrari():
    print("Nice choice!; a ferrari")
    print("This will cost you" + " " + str(ferrari_cost))
    print("Would you like to go ahead and buy it?")
    choice = input(">")
    if "yes" in choice:
        new_balance = cash - ferrari_cost
        print("Your new balance will be" + " " + str(new_balance))
    elif "no" in choice:
        car_dealer()
    else:
        print("Give me a straight yes or no!")
        exit(0)

def lambo():
    print("Nice choice a Lamborghini!")
    print("This will cost you" + " " + str(lambo_cost))
    print("Would you go  ahead and buy it?")
    choice = input(">")
    if "yes" in choice:
        new_balance = cash - lambo_cost
        print("Your new balance will be" + " " + str(new_balance))
    elif "no" in choice:
        car_dealer()
    else:
        print("I dont know what that means")
        exit(0)


#Car dealer entrance; this function will call to other functions based on your choice
   
def car_dealer():
    print("you enter a car dealer who sells only ferrari and lamborghini")
    print("which one will you pick?")
    choice = input(">")
    if "Ferrari" in choice:
        ferrari()
        Car_bought = True
        print("You bought a Ferrari Today!")
    elif "Lambo" in choice:
        lambo()
        Car_bought = True
        print("You bought a lambo today!")
    else:
        Car_bought = False
        exit(0)

car_dealer()

