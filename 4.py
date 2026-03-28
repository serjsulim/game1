flag = True
n=0
while flag:
    try:
        a = int(input('Уведи натуральне число -> '))
        if a > n:
            n = a
        if a < 1:
            flag = False
    except:
        flag = False
if n == 0:
    print('Немає жодного натурального числа')
else:
    print(f'Найбільше число було: {n}')
        
    
   
