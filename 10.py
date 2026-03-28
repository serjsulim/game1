def proste(tcislo):
    for i in range(2,tcislo):
        if tcislo % i == 0:
            return False
    return True
    
n = int(input('Уведи число -> '))
if proste(n):  
    print(f'{n} - просте число')
else:
    print(f'{n} - не просте число')

