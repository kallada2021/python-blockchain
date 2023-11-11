a = 1 - 0.9 - 0.1

b = 1 - 1/2

text = """this is text
    Line two
!!!"""

# list
blockchain = [1, 8.6, 5.2]
blockchain = [1, 8.6, 5.2, 10]

blockchain.append(3)

print(blockchain[1] + 2)

blockchain.pop()  # removes last element of the list

print(blockchain)
print(blockchain[1])
print(a)
print(b)
print(text)

name = input("Please enter your name.")
age = int(input("Please enter your age."))

def get_data(name, age):
    print(f"{name} is {age} years old")
    years = age / 10
    decades = int(years)
    print(f"{name} has been alive for {decades} decades.")

get_data(name, age)