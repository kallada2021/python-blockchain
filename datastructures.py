simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
print(simple_list)
del(simple_list[0])
print(simple_list)

d = {"name": "Omar", "age": 29}
print(d.items())

print([el for el in d])

for k, v in d.items():
    print(k,v)

t = (1,2,3)
print(t.index(1))

# s = {"one","two","one"}
# print(s)

new_list = [True, True, False]
print(any(new_list))
print(all(new_list))

numbers = [1,2,3,-5]
print([el for el in numbers if el > 0])
print(all([el > 0 for el in numbers]))

new_set = {"Max", "Ali", 1}
print(new_set)

set_list = [el for el in new_set]
print(set_list)

for el in new_set:
    print(el)

a, b, c = new_set
print(f"a = {a} b = {b} c = {c}")
# print(new_set[0])
funds = 150.45435
print("Funds: {:.2f}".format(funds))
