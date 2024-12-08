#Polymorphism
class RoadUser:
    def User(self):
        print("Japanese Domestic Market")
        print(self)
class Truck(RoadUser):
    def User(self):
        print("Isuzu Giga Forward 6BG1")

class Car(RoadUser):
    def __init__(self, Make, Model, Engine):
        self.Make = Make
        self.Model = Model
        self.Engine = Engine
        
   
    def __str__(self):
        return self.Make + " " + self.Model + " " + self.Engine
    def AllCars(cars):
        for car in cars:
            print(car)
roadusers = [Car("Toyota" , "Tamaraw FX" , "3C Turbo") , 
             Car("Hyundai" , "Starex" , "D4BB Ordinary") ,
             Truck()]

for roaduser in roadusers:
    roaduser.User()
