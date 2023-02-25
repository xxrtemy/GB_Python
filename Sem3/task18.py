
import random
list = []
list_diff = []

lenght_value = int(input('Введите кол-во элементов массива: '))
x_value = int(input('Введите X: '))

for i in range(lenght_value):
    list.append(random.randint(1, 10))
print(list)

for i in range(len(list)):
    list_diff.append(abs(list[i] - x_value))

min_value = min(list_diff)
index = list_diff.index(min_value)

print(f'Максимально близкий к Х элемент: {list[index]}')