
import random
count = 0
list = []

lenght_value = int(input('Введите кол-во элементов массива: '))
x_value = int(input('Введите X: '))

for i in range(lenght_value):
    list.append(random.randint(1, 10))
print(list)

for i in range(len(list)):
    if x_value == list[i]:
        count += 1
print(f'В созданном массиве {count} раз встречается X')