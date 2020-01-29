spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue #This causes the while to start again without going down!
    print(f"This is spam {spam}")
