class Tour:
    def __init__(self, tour_name, tour_type, country, destination_cities, price, days):
        self.tour_name = tour_name
        self.tour_type = tour_type
        self.country = country
        self.destination_cities = destination_cities
        self.price = price

    def update_tour_type(self, new_tour_type):
        self.tour_type = new_tour_type
        return self.tour_type
    
    def add_destination_city(self, destination_city):
        self.destination_cities.append(destination_city)
        return self.destination_cities
    
    def __repr__(self):
        return self.tour_name



tour = Tour("Bahamas Vacation","cruise", "Bahamas", ["Nassau"], 1000, 5)
print(tour.tour_name)

t1 = tour.update_tour_type("land")
print(t1)

cities = tour.add_destination_city("CatIsland")
print(cities)

thai_tour = Tour("Thailand Vacation","Beach Tour", "Thailand", ["Bangkok"], 3500, 5)
print(thai_tour.destination_cities, thai_tour.price)

thai_city = thai_tour.add_destination_city(destination_city="Chiang Mai")
# print(thai_city)


tours = [tour, thai_tour]
all_cities = []
for t in tours:
    all_cities.extend(t.destination_cities)

print(all_cities)
# print(tours)