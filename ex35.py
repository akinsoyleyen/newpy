from sys import exit

def gold_room():
    print("If this room is full of gold, how much would you take?")

    choice = input(">")
    if True: #! Burada demek istiyorki ; eger Choice = herhangi birsey ise. Yani Bos degilse
        how_much = int(choice)
    else:
        print("Man, learn to type a number")
    
    if how_much < 50:
        print("Nice, you are not greedy, you win")
        exit(0)
    else:
        print("You greedy bastard!")

def bear_room():
    print("There is a bear here.!")
    print("The bear has a bunch of honey!")
    print("The Fat bear is infront of another door")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(">")

        if choice == "take honey":
            print("the bear looks at you and slaps your face off") #died
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now")
            bear_moved = True #bear hareket etti
        elif choice == "taunt bear" and bear_moved:
            print("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room() #Bununla loop tan escape etmis oluyoruz.
        else:
            print("I got no idead what that means.")

def cthulhu_room():
    print("Here you see the great evi Cthulhu")
    print("hE, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        print("Well that was nasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print("Which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve.....")

start()

        