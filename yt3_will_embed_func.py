# Program from Youtube Videos - WilliamFiset
# Embedding Functions

def add_ten(num):
    return  num + 10

def double(num):
    return num * 2

def triple(num):
    return num * 3


number = 3
result1 = add_ten(double(triple(number)))
print(result1)

result2 = triple(double(add_ten(number)))
print(result2)