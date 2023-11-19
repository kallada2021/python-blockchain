a = 1 - 0.9 

# print(a)
b = 1 - 1/2

text = """this is text
    Line two
!!!"""

# print(a != 1)
# print(a is 1)

data = [1, 1.5, 3.4]
more_data = [1, 1.5, 3.4]
# print(data == more_data)
# print(data is more_data)
# print(data is not more_data)
# print(1 in data)
# print(9 not in data)

# list
blockchain = [1, 8.6, 5.2]
blockchain = [1, 8.6, 5.2, 10]

blockchain.append(3)

print(blockchain[1] + 2)

# blockchain.pop()  # removes last element of the list

print(blockchain)
print(blockchain[1])
# print(a)
# print(b)
# print(text)

# name = input("Please enter your name.")
# age = int(input("Please enter your age."))

def get_data(name, age):
    print(f"{name} is {age} years old")
    years = age / 10
    decades = int(years)
    print(f"{name} has been alive for {decades} decades.")

#get_data(name, age)

simple_list = [1,2,3,4]
dup_list = [el * 2 for el in simple_list]

print(dup_list)

calc_item = [1,2]
calc_list = [el * 2 for el in simple_list if el in calc_item]
print(calc_list)