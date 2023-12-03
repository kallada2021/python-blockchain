class Car:
    # top_speed = 100
    # warnings = []
    
    def __init__(self, starting_speed=150):
        self.top_speed = starting_speed
        self.warnings = []
        
    def __repr__(self):
        print("Printing car")
        return f"Top Speed {self.top_speed} warnings {self.warnings}"
    
    def add_warning(self, warning):
        if len(self.warnings) >= 0:
            self.warnings.append(warning)
            
    def get_warnings(self):
        return self.warnings
    
    def drive(self):
        print("Driving slower than {}".format(self.top_speed))
  

car1 = Car(200)
car1.drive()  

car1.warnings.append("New Warnings")
car1.add_warning("Slow down.")
 
print(car1.warnings)
print(f"car1 {car1}")
print(f"car1 dict {car1.__dict__}")

car2 = Car()
car2.drive()
print(car2.warnings)
print(car2.get_warnings())
print(car2.__dict__)
