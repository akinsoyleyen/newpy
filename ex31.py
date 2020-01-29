print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There is a giant bear here eating a cheese cake")
    print("What do you do?")
    print("1.Take the cake")
    print("2.Secream at the bear")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good joB!")
    elif bear == "2":
        print("the bear eats your legs off. Good Job")
    else:
        print(f"Well, doing {bear} is probably better")
        print("Bear runs away!")

elif door == "2":
    print("You stare into the endless abyss at Cthulus retina")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("yOUR BODY SURVIVES POWERED BY A Mind of jello")
        print("good job!")
    else:
        print("The insanity rots your eyes into a pool of much")
        print("Good jOB")
else:
    print("You stumble around and fall on a knife and die. Good job!")
    
