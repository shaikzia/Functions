# Program from Youtube Videos - code Basics
# Program to use default args for a function

# here b is called the default argument
def sum (a, b=10):
    total = a + b
    return total

# Pass the value to b
print(sum(11, 11))

# If no value is passed, b will get the defualt value
print(sum(11))


def product(a,b=10,c=10):
    res = a * b * c
    return  res

print(product(9))
