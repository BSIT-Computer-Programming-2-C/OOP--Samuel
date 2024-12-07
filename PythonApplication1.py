class Car:
    def __init__(self, Make, Model, Engine):
        self.Make = Make
        self.Model = Model
        self.Engine = Engine
        
    @property
    def Make(self):
        print("getting Make")
        return self._Make
    @Make.setter
    def Make(self , Make):
        print("setting Make")
        self._Make = Make
    def __str__(self):
        return self.Make + " " + self.Model + " " + self.Engine
    def AllCars(cars):
        for car in cars:
            print(car)
cars = [Car("Toyota" , "Tamaraw FX" , "3C Turbo") , Car("Hyundai" , "Starex" , "D4BB Ordinary")]

Car.AllCars(cars)
