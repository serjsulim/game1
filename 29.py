def stan_skladu (q):
    for i in range(len(q)):     # 0, 1, 2
        for j in range(len(q[i])):    # 0, 1, 2 , 3, 4
            print(q[i][j], end = " ")
        print(" ")
    return 
    
def rezerv(w):
    riad = int(input('Напиши ряд -> '))
    if riad > len(w):        # len(w) це кількість рядків (тут 3 штуки)
        print('Такого ряду немає')
        return
    misce = int(input('Вкажи місце -> '))
    if misce > len(w[0]):     # len(w[0])  це довжина нульового рядка (у даному випадку 5)
        print('Такого місця немає')
        return
    riad -= 1
    misce -= 1
    if w[riad][misce] == 0:
        w[riad][misce] = 1
        print(f"Місце {riad}:{misce} зарезервовано")
    else:
        print('Вибачте, але це місце вже зайняте')


n = 3      # кількість рядів
m = 5      # кількість місць (стовпців)
a = []
for nomer_riadka in range(n):
    a.append([])
    for nomer_stovpcia in range(m):
        a[nomer_riadka].append(0)


print(stan_skladu(a))
rezerv(a)
print(stan_skladu(a))
