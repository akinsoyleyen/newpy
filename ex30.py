people = 30
cars = 40
trucks = 15
#Eger arabalar insanlardan coksa
if cars > people:
    print("We should take the cars")
#Eger insanlar arabalardan coksa
elif cars < people:
    print("We should not take the cars")
#Hicbiri degilse
else:
    print("We cannot decide")

if trucks > cars:
    print("Thats too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still cant decide")

if people > trucks:
    print("Allright, lets just take the trucks")
else:
    print("Fine, lets stay home then.")

#deneme
