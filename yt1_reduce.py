# Programs on Reduce functions from Youtube
from functools import reduce
# Find the Product of a list using Reduce - Indian Pythonista
mylist = [1,2,3,4,5,6]
prod = reduce(lambda x,y: x*y,mylist)
print(prod)
print('********End of program*************')

# Addition of list elements
mylist2 = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y, mylist2)
print(sum)