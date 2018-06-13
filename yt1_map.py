# Programs on map functions from Youtube
# Centigrade to Fahrenheit - Socratica

temps = [("Berlin", 29),("London",17), ("Hyderabad",45)]
c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

res = list(map(c_to_f,temps))
print(res)
print('********End of program*************')

# Square of a list - Joe James
numbers_list = [4,5,6,7]
square = lambda x: x**2
s2_res = list(map(square,numbers_list))
print(s2_res)
print('********End of program*************')



