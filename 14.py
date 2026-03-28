def bilshe(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 'Числа рівні'
    
a = float(input('Уведи перше число -> '))
b = float(input('Уведи друге число -> '))
print(f'Більше число: {bilshe(a, b)}')