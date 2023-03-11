
def expanentation(a , b):
    if b == 00 :
        return 1
    else:
        return a * expanentation(a, b -1)
    
a = int(input('Введите число: '))
b = int(input('Введите степень числа: '))

print(expanentation(a,b))

