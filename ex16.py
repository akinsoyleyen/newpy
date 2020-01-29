from sys import argv

script, filename = argv

print(f"We are going to delete {filename}")
print("If you dont want that, hit CTRL-C")
print("If you do want that hit RETURN")

input("?")

print("Opening the file...")

target = open(filename, 'w')

print("Truncating the file, GoodBye!")
target.truncate()

print("Now im going to ask you for three lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("Im going to write these to the file")

target.write(line1 + "\n" + line2 + "\n" + line3)


print("and finally, we close it")
target.close()
