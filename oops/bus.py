from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, starting_speed=100):
        super().__init__(starting_speed)
        self.passengers = []
        
    def add_group(self, passengers):
        self.passengers.extend(passengers)
        

bus1 = Bus(150)
bus1.add_warning("Test")
bus1.add_group(["Max","Omar"])
print(bus1.passengers)
bus1.drive()
print(bus1.get_warnings())
