class Tour:
    def __init__(self, tour_name, tour_type, country, destination_cities, price):
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
        return f"{self.tour_name},{self.country}"
    
    def change_tour_price(self, new_tour_price):
        self.price = new_tour_price
        return self.price



tour = Tour("Bahamas Vacation","cruise", "Bahamas", ["Nassau"], 1000)
print(tour)
print(tour.tour_name)

t1 = tour.update_tour_type("land")
print(t1)

cities = tour.add_destination_city("CatIsland")
print(cities)

thai_tour = Tour("Thailand Vacation","Beach Tour", "Thailand", ["Bangkok"], 3500)
print(thai_tour.destination_cities, thai_tour.price)

thai_city = thai_tour.add_destination_city(destination_city="Chiang Mai")
# print(thai_city)

new_price = thai_tour.change_tour_price(5000)
print(new_price)

tours = [tour, thai_tour]
all_cities = []
for t in tours:
    all_cities.extend(t.destination_cities)

print(all_cities)
# print(tours)

tour_prices = [tour.price, thai_tour.price]
all_prices = []
for price in tour_prices:
    all_prices.append(price)

print(all_prices)

# Write a class that inherits from Tour

class WaterSports(Tour):
    def __init__(self, tour_name, tour_type, country, destination_cities, price, days):
        self.days = days
        super().__init__(tour_name, tour_type, country, destination_cities, price)
    
    def increase_price(self, new_price):
        self.price += new_price

sunset_tour = WaterSports("Dinner on the Ocean", "Couples Tour", "Jamaica", "Montega Bay", 50, 1)
sunset_tour.increase_price(50)
print(f"New price for {sunset_tour.tour_name} is ${sunset_tour.price}")


day_tour = WaterSports("Scuba Diving", "Motorized Water Sports", "Jamaica", "Montega Bay", 500, 1)
print(day_tour.__dict__)

parasailing_tour = WaterSports("Parasailing", "Motorized Water Sports", "Jamaica", "Montega Bay", 600, 0.5)
print(parasailing_tour.__dict__)

# Print list of watersports with names and price 
activities_price = [day_tour.tour_name, day_tour.price, parasailing_tour.tour_name, parasailing_tour.price]
print(activities_price)
all_activities_price = []
for price in activities_price:
    all_activities_price.append(price)

print(all_activities_price)

activities_prices = [day_tour.price, parasailing_tour.price]
# print(activities_prices)
all_activities_prices = []
for price in activities_prices:
    all_activities_prices.append(int(price) + 50)

print(all_activities_prices)