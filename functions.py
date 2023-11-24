num_list = [1,2,3,4]

def multiply(el):
    return el * 2 

newmap = map(multiply, num_list)
print(list(newmap))

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
