class Car:
    def __init__(self, color, model, weight):
        self.color = color
        self.model = model
        self.weight = weight
        self.mileage = 0

    def drive(self):
        self.mileage += 10
        print(f"The {self.color} car has done a drive of 10 KM, mileage is now {self.mileage}")

class SportsCar(Car):
    
    def drive(self):
        self.mileage += 20
        print(f"The {self.color} cool sportcar has done a drive of 20 KM, mileage is now {self.mileage}")

ferrari = SportsCar("yellow", "F8", "1.3 ton")
ferrari.drive()
ferrari.drive()
