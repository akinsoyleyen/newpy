class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name , str(self.age))

    def sit(self):
        print(f'now {self.name} is sitting down')

dog_1 = Dog("Willie",10) 
#!Buradaki dog_1 bir instance oluyor yani bunu yazidigmizda artik dog_1 isimli bir kopek olusturmus oluyoruz
dog_1.sit()
#! When python reads .sit() it is looking for that function(method) inside the Dog class.