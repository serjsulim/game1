def suma(n):
    summma = 0
    for i in range(1,n+1):
        summma += i
    return summma


n = int(input('Уведи натуральне число ->'))
print(f'Сума перших {n} чисел дорівнює {suma(n)}')