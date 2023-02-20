
value = int(input('Введите номер вашего билета: '))
check_value = value
count = 0
while check_value > 0:
    count += 1
    check_value //= 10
counter = 1
sum1 = 0
sum2 = 0   
if count != 6: 
    print('Введенный билет не существует...')
    exit()
while counter <= 3:
    sum1 += value % 10
    value //= 10
    counter +=1
    if counter == 4:
        break 
while counter > 3:
    sum2 += value % 10
    value //= 10
    counter +=1
    if counter == 7:
        break
if sum1 == sum2:
   print('Введенный билет cчастливый')
else:
    print('Введенный билет не является счастливым')    