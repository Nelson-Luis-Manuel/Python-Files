class Dog:
    def __init__(self,name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

myDog = Dog('Rover')
otherDog = Dog ('Rex')

myDog.speak() 
otherDog.speak()