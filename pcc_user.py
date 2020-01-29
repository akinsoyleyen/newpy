class User:
    def __init__(self, username, password, height, weight):
        self.username = username
        self.password = password
        self.height = height
        self.weight = weight
    def describe_user(self):
        print(f"Hello your username is {self.username} and password is {self.password}")
    def greet_user(self):
        print(f"Hello {self.username} Wellcome to Python")

user_1 = User("Akin","esrakin2002", "168cm", "80kg")
user_1.describe_user()
    