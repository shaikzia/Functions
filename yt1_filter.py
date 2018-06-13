# Programs on filter functions from Youtube

# Filter odd numbers from a list - Indian Pythonista
mylist = [1,2,3,4,5,6,7,8,9]
odd_nos = list(filter(lambda x: x % 2,mylist))
print(odd_nos)
print('********End of program*************')

# Filter greater than , less than Average  - Socratica
import statistics
data = [0.5,1.5,2.5,3.5]
avg = statistics.mean(data)
print(avg)

gt_avg = list(filter(lambda x: x > avg, data))
print(gt_avg)

lt_avg = list(filter(lambda y: y < avg, data))
print(lt_avg)

