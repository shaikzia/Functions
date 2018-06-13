# Program from Youtube Videos - code Basics
# Program to know local and global variables

# This is Global Variable
g_total = 999

def sum(a,b):
    print("a: ", a)
    print("b: ", b)

# This is a local variable
    total = a + b
    print("Total inside the function: ", total)

sum(b = 10, a = 20)

print("Total from Global Variable is: ", g_total)