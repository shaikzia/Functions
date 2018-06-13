# Programs on Lambda functions from Youtube
# Normal function written in a single line
def addition(a,b,c): return a+b+c
print(addition(1,2,3))

# Same function written with Lambda keyword
g = lambda a,b,c: a+b+c
y = g(1,2,3)
print(y)

# Square of a number using Lambda - WilliamFiset
square = lambda x: x  *x
print(square(99))

# Remove duplicates
remove_dups = lambda iterable: set(iterable)
print(remove_dups('rrrrrrrrrooooooooooottttttttt'))
print(remove_dups('thisisisisaduppplicaaate'))

# Avg of list - Indian Pythonista
mylist = [1,2,3,4,5,6]
avg = lambda l: sum(l) / len(l)
print(avg(mylist))

# Multiple Arguments to lambda - Socratica
f = lambda a,b,c: lambda x: a*x**2 + b*x + c
print(f(1,2,3)(3))

