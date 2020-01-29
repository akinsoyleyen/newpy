class MyCars:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odo_read = 0
    
    def describe_car(self):
        description = print(f"Your car is {self.manufacturer} , {self.model} model and produced in the year of {self.year}")
    def read_odo(self):
        print(f"Your car has {self.odo_read} km's on it")



car_1 = MyCars("Honda", "S2000", "2008")
print(car_1.describe_car())
MyCars.odo_read = 10
car_1.read_odo()