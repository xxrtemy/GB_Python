
def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

list_1 = []
list_2 = []
union_set = set()

lenght_value_1 = int(input('Введите кол-во элементов 1-го массива: '))
lenght_value_2 = int(input('Введите кол-во элементов 2-го массива: '))

for i in range(lenght_value_1):
    list_1.append(int(input('Введите элементы 1-го массива: ')))

for i in range(lenght_value_2):
    list_2.append(int(input('Введите элементы 2-го массива: ')))
  
set_1 = set(quicksort(list_1))
set_2 = set(quicksort(list_2))

union_set = set_1.union(set_2)
union_tuple = tuple(union_set)

print(quicksort(union_tuple))