# Program from Youtube Videos - code Basics
# Program to calculate the expenses of Tom and Jerry

list1 = input("Enter list1")
list2 = input("Enter list2")

tom = [int(x) for x in list1.split()]
jerry = [int(x) for x in list2.split()]

print(tom)
print(jerry)
# Define a Function to find the total
def calculate_exp(exp):
    total = 0
    for item in exp:
        total = total + item
    return  total

toms_total = calculate_exp(tom)
jerrys_total = calculate_exp(jerry)

print(toms_total)
print(jerrys_total)