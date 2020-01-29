class Person:

    def __init__(self, sex, name, height, weight): #This is to create the human
        self.sex = sex
        self.name = name
        self.height = height
        self.weight = weight
    
    def person_description(self): #This is to print the human description
        print(f"{self.sex}")
        print(f"{self.name}")
        print(f"{self.height}")
        print(f"{self.weight}")

person_1 = Person('Male', 'Akin', '168cm', '80')
print(f"{person_1.person_description()}")
