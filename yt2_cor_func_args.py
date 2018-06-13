# Program from Youtube Videos - corey schafer
# Function 1
def hi_func(greeting):
    return '{} Function'.format(greeting)

print(hi_func('Hello'))

# Function 2
def hi_func2(greeting, message):
    return '{} Function {}'.format(greeting, message)

print(hi_func2('Hello', ', How are you?'))

#Function 3
def hi_func3(greeting, name ='YOU'):
    return '{} {}'.format(greeting, name)

print(hi_func3('Hey'))
print(hi_func3('Hey', name = 'Zia'))


#Function 4
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Maths','Science', name='Faiz', age='7')


#Function 5
def stud_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ['Maths','Science','Arts']
info = {'name':'Zairah','age': 5}

stud_info(*courses,**info)