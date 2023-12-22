class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def change_restaurant_name(self, new_restaurant_name):
        self.restaurant_name = new_restaurant_name
        return self.restaurant_name
    
    def open_restaurant(self, open_status):
        self.restaurant_status = open_status
        return self.restaurant_status
    
    def meal_time(self, time_of_the_day):
        if time_of_the_day == "evening":
            return "dinner!"
        elif time_of_the_day == "noon":
            return "lunch!"
        else:
            return "Refer to hours of operation!!"
        
class IceCreamStand(Restaurant):
    def __init__(self, ice_cream_stand_name, flavors):
        super().__init__(ice_cream_stand_name, "Ice Cream")
        self.flavors = flavors
    
    def icecream_flavors(self):
        return self.flavors
        
    

restaurant = Restaurant("India House", "Indian")
print(restaurant.restaurant_name, restaurant.cuisine_type)

restaurant_status = restaurant.open_restaurant("Open")
serving = restaurant.meal_time("noon")
print(f"{restaurant.restaurant_name} is now {restaurant_status} for {serving}")

previous_name  = restaurant.restaurant_name
restaurant_new_name = restaurant.change_restaurant_name("Chennai Cafe")
print(f"{previous_name} is now {restaurant.restaurant_name}")

restaurant_thai = Restaurant("Thai House", "Thai Food")
print(f"Restaurant name is {restaurant_thai.restaurant_name}", f" and Cuisine type is {restaurant_thai.cuisine_type}")

stand_name = IceCreamStand("Rita's", "Mango")
print(f"{stand_name.change_restaurant_name('Dairy Queen')} is now serving {stand_name.icecream_flavors()} flavored icecream!!")