# Program from Youtube Videos - sentdex
# Program for a basic function
def example():
    print('This is a basic function')

    z = 3+3
    print(z)
example()
print('********End of program*************')

# Adding two numbers, passing parameters
def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is',num1)
    print('num2 is', num2)
    print(answer)

simple_addition(3,5)
print('********End of program*************')

# Adding 2 numbers, with default parameters
def add_numbers1(num1,num2):
    pass

def add_numbers(num1,num2 = 5):
    print(num1,num2)

add_numbers(2)
add_numbers(4,6)
print('********End of program*************')

# Multi parameters
def window(width,height,font='TNR',bgc='W'):
    print(width,height,font,bgc)

window(50,30)
window(50,30,'BCR')
window(50,30, bgc='X')