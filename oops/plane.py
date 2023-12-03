from vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, destination, starting_speed=150):
        super().__init__(starting_speed)
        self.crew = []
        self.destination = destination

    def add_crew(self,crew):
        self.crew.extend(crew)
        return self.crew
    
plane1 = Plane("Mexico")
plane1.add_crew(["Pilot","Co-Pilot","Flight Engineer"])
print(plane1.add_crew(["Flight Attendant"]))