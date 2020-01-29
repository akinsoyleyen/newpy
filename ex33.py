i = 0
numbers = []

def below_high_number(high_number):
    
    while i < high_number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now: ", numbers)
        print(f"at the bottom i is {i}")

below_high_number(6)
print("The Numbers:  ")

for num in numbers:
    print(num)