from vehicle import Vehicle
class Car(Vehicle):
    # top_speed = 100
    # warnings = []
    
    def __init__(self, engine_type, starting_speed=150, fuel_type="gas", weather="Clear"):
        super().__init__(starting_speed=starting_speed)
        self.engine_type = engine_type
        self.fuel_type = fuel_type
        self.weather = weather
    
    def get_fuel(self):
        if self.fuel_type == "gas":
            print("Running low on fuel.. go to the nearest gas station.")
        else:
            print("Running low on charge.. go to the nearest charging station.")
    
    def turnon_wipers(self):
        if self.weather == "Snowing" or self.weather == "Raining":
            return "Wipers are turned on"
        else:
            return "Wipers are turned off."
            

car1 = Car(200)
car1.drive()  

car1.warnings.append("New Warnings")
car1.add_warning("Slow down.")
 
print(car1.warnings)
print(f"car1 {car1}")
print(f"car1 dict {car1.__dict__}")

car2 = Car(engine_type="V6")
car2.drive()
print(car2.warnings)
print(car2.get_warnings())
print(car2.__dict__)

car3 = Car("V4",60, "electric", "Raining")
car3.add_warning(f'Driving slower than 150. Current car speed is: {car3.top_speed}')
car3.add_warning(f'Minimum spped is 70 mph.. you are driving like a grandpa.')
car3.add_warning(f'It is raining...wipers will be turned on.')
print(car3.engine_type)
print(car3.get_warnings())
car3.get_fuel()
car3.turnon_wipers()
print(car3.turnon_wipers())