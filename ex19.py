def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have cheese count {cheese_count}")
    print(f"You have {boxes_of_crackers}, boxes of crackers")
    print("Man thats enough for a party!")
    print("Get a blanket.\n")

print("We can pass the numbers directly to the function")
cheese_and_crackers(10,30)

print("We can make it do the math")
cheese_and_crackers(10+20, 30+40)

print("Or we can pass variable to the argument")
amount_of_cheese = 30
amount_of_crackers = 40
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

