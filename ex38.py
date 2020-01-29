ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print("Wait there are not 10 things in that list. Let's fix that")

stuff = ten_things.split(' ') #This will return a list of ten_things
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: #!stuff listesinin madde sayisi 10 olmadikca assagidaki kodu calistirir.
    next_one = more_stuff.pop() #more_stuff listesinin sonundaki 'Boy' kopartti ; ve artik next_one = 'boy' oldu
    print("Adding:", next_one)
    stuff.append(next_one) #next_one yani 'Boy' ekle!
    print(f"There are {len(stuff)} items now") #artik stuff listesinde 7 urun var.

print(f"There we go {stuff}")

print("Lets do some things with the stuff")

print(stuff[1]) #?Orange olmasi lazim
print(stuff[-1]) #TODO Corn olmasi lazim
print(stuff.pop()) #!Corn olmasi lazim
print(" ".join(stuff)) #
print("#".join(stuff[3:5]))




