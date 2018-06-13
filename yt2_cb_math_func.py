# Program from Youtube Videos - code Basics
# Program to perform the Math Operations

# Sum
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))

def sum(a,b):
    total = a + b
    return  total

print(sum(a,b))

# n = sum(b=10, a=12)
# print(n)

# Difference
def diff(a,b):
    if a > b:
        res = a - b
        return res
    else:
        res = b - a
        return  res

print(diff(a,b))

# Mutiplication
def mul(a,b):
    prod = a * b
    return prod

print(mul(a,b))

# Division - divide a by b
def div(a,b):
    if b != 0:
        res = a / b
        return res
    else:
       return 'Division not possible'


print(div(a,b))