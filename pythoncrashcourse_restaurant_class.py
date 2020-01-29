class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served): #!method1
        self.restaurant_name = restaurant_name #attribute1
        self.cuisine_type = cuisine_type #attribute2
        self.number_served = number_served #attribute3

    def describe_restaurant(self): #!method2
        print(f"the name of the restaurant is {self.restaurant_name} and cuisine type is {self.cuisine_type}")

    def open_restaurant(self): #!method3
        print(f"The restaurant {self.restaurant_name} is open!")

    def set_number_served(self, added_miles):
        self.number_served = added_miles

    def numbers_served(self):
        print(f"Restaurant {self.restaurant_name} has served its customers {self.number_served} times")

restaurant = Restaurant("Rina", "Fish","0") #?instance created!
print(f'{restaurant.restaurant_name}  {restaurant.cuisine_type}')


restaurant_1 = Restaurant("Big Chefs", "American",0)
restaurant_1.describe_restaurant()
restaurant_1.set_number_served(5)
restaurant_1.numbers_served()

restaurant_2 = Restaurant("McDonalds", "Fast Food", 7)
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant("Burger King", "Fast Food",8)
restaurant_3.describe_restaurant()

