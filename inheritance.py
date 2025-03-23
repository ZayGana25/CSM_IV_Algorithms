# Isaiah Lugo  
# CSM IV - Algorithms
# Assignment 1

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is a {self.year} {self.make} {self.model}.")

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors, max_speed):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
        self.max_speed = max_speed

    def car_details(self):
        print(f"This {self.make} {self.model} has {self.number_of_doors} doors and a max speed of {self.max_speed} mph.")

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, drive_type):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        self.drive_type = drive_type

    def truck_info(self):
        print(f"This {self.make} {self.model} truck has a cargo capacity of {self.cargo_capacity} tons and {self.drive_type} drive.")

# Example Usage
vehicle_1 = Vehicle("Toyota", "Supra", 2021)
car_1 = Car("Ford", "Mustang GT", 2024, 2, 180)
truck_1 = Truck("Ford", "F-150", 2023, 1.1, "4 wheel")

vehicle_1.display_info()  # "This is a 2021 Toyota Supra."
car_1.car_details()       # "This Ford Mustang has 2 doors and a max speed of 180 mph."
truck_1.truck_info()      # "This Ford F-150 truck has a cargo capacity of 1.1 tons and 4 wheel drive."
