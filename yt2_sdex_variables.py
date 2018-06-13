# Program from Youtube Videos - sentdex

# Program using functions with Global and local variables

g = 6

def example():
    print(g)

example()
print('***************')

def example1():
    print(g)
    print(g+5)

example1()
print('***************')

def example2():
    global g
    print(g)
    g += 6
    print(g)

example2()
print('***************')


a = 10
def example3():
    globvar = a
    print(globvar)
    globvar += 7
    print(globvar)
    return globvar

e = example3()
print(e)
print('***************')