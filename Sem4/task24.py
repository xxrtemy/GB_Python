
import random

count = int(input())
list = []
list_count = []

for i in range(count):
    list.append(random.randint(1,100))
print(list)

for i in range(len(list) - 1):
    list_count.append(list[i-1] + list[i] + list[i+1])
list_count.append(list[-2] + list[-1] + list[0])
print(max(list_count))