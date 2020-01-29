which_car = input("""Which Car would you like to choose?
A Ferrari or a Lambo?""")


if which_car == "Ferrari":
    print(f"Good choice with the {which_car}")
    which_color = input(f"Which Color would you like your fast {which_car} to be? Red or Yellow?")
    if which_color == "Red":
        print(f"Nice choice of color: {which_color} for your {which_car}")
    elif which_color == "Yellow":
        print(f"Would not be my favourite for {which_car} in {which_color}")
    else:
        print("Choose Red or Yellow")
elif which_car == "Lambo":
    print(f"Good Choice man! Your car ise {which_car}")
    which_color = input(f"Which Color would you like your fast {which_car} to be? Red or Yellow?")
    if which_color == "Red":
        print(f"Nice choice of color: {which_color} for your {which_car}")
    elif which_color == "Yellow":
        print(f"Would not be my favourite for {which_car} in {which_color}")
    else:
        print("Wrong color choice man!")
else:
    print("Choose Ferrari or Lambo")
    


