class Vehicle():
    def __init__(self, starting_speed=150,):
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
  