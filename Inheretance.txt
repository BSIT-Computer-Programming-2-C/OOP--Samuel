#Inheritance
class RoadUser:
    def User(self):
        print("Japanese Domestic Market")
        print(self)

class Car(RoadUser):#class RoadUser is inherited in this class
    def __init__(self, Make, Model, Engine):
        self.Make = Make
        self.Model = Model
        self.Engine = Engine
        
   
    def __str__(self):
        return self.Make + " " + self.Model + " " + self.Engine
    def AllCars(cars):
        for car in cars:
            print(car)
cars = [Car("Toyota" , "Tamaraw FX" , "3C Turbo") , Car("Hyundai" , "Starex" , "D4BB Ordinary")]


cars[0].User(), cars[1].User()
