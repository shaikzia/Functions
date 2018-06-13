# Program from Youtube Videos - WilliamFiset
# Recursive Functions

def double(x):
    if x == 0:
        return  0

    return double(x-1) + 2

print(double(4))
print('*******End of program**********')

# Triangle numbers
def triangle_numbers(n):
        if n == 0: return  0

        return triangle_numbers(n-1) + n

for n in range(5):
    print(triangle_numbers(n))
print('*******End of program**********')

# Sum of a digits in number
# Normal way using a function
# def sum_digits( num ):
#     s = 0
#     while num:
#         s = s + num % 10
#         num //= 10
#     return s
# y = sum_digits(343)
# print(y)

# Sum of a digits in number using Recursion
def sum_digits2( num ):
    if num == 0: return 0
    return sum_digits2(num // 10) + num % 10

print((sum_digits2(343)))
print((sum_digits2(12345)))
print('*******End of program**********')

# Count letter in a string
# Normal way using a function
# def count_string(str):
#     x_count = 0
#     for char in str:
#         if char == 'x':
#             x_count += 1
#     return x_count
# y = count_string('yxyxyxyxyxxxx')
# print(y)

# Count letter in a string using recursion
def count_string_rec(string):
    if string == '': return  0
    last_letter = string[-1]
    if last_letter == 'x':
        return count_string_rec(string[:-1]) + 1
    return count_string_rec(string[:-1]) + 0
print(count_string_rec('xxxyxxyxy'))
print('*******End of program**********')

# factorial of a number, normal way
# num = 5
# fac = 1
# for i in range(1, num+1):
#     fac = fac * i
# print(fac)

## Factorial of a num using Recursion
n = int(input('Enter number: '))
def fact(n):
    if n==1:
        return n
    elif n==0:
        return 1
    else:
        return n * fact(n-1)

x = fact(n)
print('factorial of', n, 'is', x)