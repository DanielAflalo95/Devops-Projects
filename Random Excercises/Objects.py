class Car:
    def __init__(self, color, model, weight):
        self.color = color
        self.model = model
        self.weight = weight
        self.mileage = 0

    def drive(self):
        self.mileage += 10
        print(f"The {self.color} car has done a drive of 10 KM, mileage is now {self.mileage}")

    def __del__(self):
        print(f"The car of model {self.model} has gone TOTAL LOSS and sent to heaven")

mazda = Car("red", "model 6", "1.5 ton")
mazda.drive()
mazda.drive()

mazda = 99  # This replaces the object (triggers destructor)

print("mazda is now just a number.")
