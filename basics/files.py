f = open("demo.txt", mode="w")  # w for write to a file r read access  a open and append to a file 
f.write("Hello from Python\n")
f.close()

with open("demo.txt", mode="r") as f:

    # content = f.readlines()
    # print(content)
    line = f.readline()
    while line:
        print(f"line {line}")
        line = f.readline()

# f.close()
print("Done")
# for line in content:
#     print(line[:-1])
