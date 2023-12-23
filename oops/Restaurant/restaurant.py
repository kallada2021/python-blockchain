class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, price):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.price = price
    
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
    
    def __lt__(self, other):
        return self.price < other.price
        
class IceCreamStand(Restaurant):
    def __init__(self, ice_cream_stand_name, flavors, price):
        super().__init__(ice_cream_stand_name, "Ice Cream", price)
        self.flavors = flavors
    
    def icecream_flavors(self):
        return self.flavors
    
    def meal_time(self, time_of_the_day):
        print(super().meal_time(time_of_the_day))
        print(f"{self.restaurant_name} is now open.")
        
    

restaurant = Restaurant("India House", "Indian", 25)
print(restaurant.restaurant_name, restaurant.cuisine_type, restaurant.price)

restaurant1 = Restaurant("Chennai Cafe", "Indian", 30)
print(restaurant.restaurant_name, restaurant.cuisine_type, restaurant.price)

print(restaurant < restaurant1)
print(restaurant1 < restaurant)

restaurant_status = restaurant.open_restaurant("Open")
serving = restaurant.meal_time("noon")
print(f"{restaurant.restaurant_name} is now {restaurant_status} for {serving}")

previous_name  = restaurant.restaurant_name
restaurant_new_name = restaurant.change_restaurant_name("Chennai Cafe")
print(f"{previous_name} is now {restaurant.restaurant_name}")

restaurant_thai = Restaurant("Thai House", "Thai Food", 18)
print(f"Restaurant name is {restaurant_thai.restaurant_name}", f" and Cuisine type is {restaurant_thai.cuisine_type}")

stand_name = IceCreamStand("Rita's", "Mango", 8)
print(f"{stand_name.change_restaurant_name('Dairy Queen')} is now serving {stand_name.icecream_flavors()} flavored icecream!!")

new_stand_name = IceCreamStand("BaskinRobbins", "Pineapple", 10)
new_stand_name.meal_time("noon")