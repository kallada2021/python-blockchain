from vehicle import Vehicle
from drivetrain import DriveTrain

class Bus(Vehicle, DriveTrain):
    def __init__(self, starting_speed=100, d_type ="AWD"):
        super().__init__(starting_speed)
        DriveTrain.__init__(self, d_type)
        self.d_type = d_type
        self.passengers = []
        
    def add_group(self, passengers):
        self.passengers.extend(passengers)

    def drive(self):
        print("Mike is driving the bus today.")
    
    def drivetrain(self):
        print(self.default_drive)
        return self.default_drive


        

bus1 = Bus(150)
bus1.add_warning("Test")
bus1.add_group(["Max","Omar"])
print(bus1.passengers)
bus1.drive()
print(bus1.get_warnings())

bus2 = Bus(80,"FWD")
bus2.drivetrain()
print(f"bus2 has a drivetype of {bus2.drivetrain()}")
