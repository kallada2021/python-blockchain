num_list = [1,2,3,4]

def multiply(el):
    return el * 2 

a = multiply(2)
print(f"a {a}")
newmap = map(multiply, num_list)
print(list(newmap))

regions = ["useast1", "uswest2", "apsouth1"]

def attach_name(region):
    return f"ds-core-{region}"

region_names = map(attach_name, regions)

for region in region_names:
    print(region)

# lambda
print(list(map(lambda el: el * 2 , num_list)))

# args and kwargs
def unlimited_args(*args, **kwargs):
    for argument in args:
        print(argument)
    for karg in kwargs.items():
        print(karg)
 
 
unlimited_args([1, 2, 3, 4, 5])  
unlimited_args(5, 6, 7, 8, 9, True, *[1,7], name="Ali", age= 33, is_programmer=False)     
