# Program from Youtube Videos - WilliamFiset
# Functions with *args and **kwargs

def add_numbers(*args): # standard convention *args, you can use your own
    print(*args)
    print(type(args))
    total = 0
    for number in args:
        total += number
    return total

result = add_numbers(1,2,3,4,5,6,7,8,9,10)
print(result)
print('********End of program*************')

def ages(**kwargs):
    print(kwargs)
    print(type(kwargs))
    avg_age = 0
    for age in kwargs.values():
        avg_age += age

    avg_age /= len(kwargs)

    return avg_age

peoples_age = ages(Zia = 39, Sajida=31, Faiz=7, Zairah=4, Saad=3)
print(peoples_age)
print('********End of program*************')


#Default parameters
def teens(gender,age,studying=True,working=False):
    print(gender,age,studying,working)

teens('Male',16)
teens('Female',18,studying=False,working=True)
print('********End of program*************')


