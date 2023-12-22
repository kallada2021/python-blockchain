import restaurant

class User:
    def __init__(self, first_name, last_name, phone_number, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
    
    def describe_user(self):
        return self.first_name, self.last_name, self.phone_number, self.email_address
    
    def greet_user(self):
        return f"{self.first_name} welcome to"

new_user = User("Thomas", "Massie", "000-000-0000", "thomas_massie@none.com")
# print(new_user.first_name, new_user.last_name, new_user.phone_number, new_user.email_address)

print(new_user.describe_user())

new_user = User("Robert", "Kraft", "000-000-0000", "robert_kraft@none.com")
print(f"{new_user.greet_user()} {restaurant.restaurant_new_name}!!")