import random

def stvory_pole():
    n = 5      # кількість рядів
    m = 5      # кількість місць (стовпців)
    a = []
    for nomer_riadka in range(n):
        a.append([])
        for nomer_stovpcia in range(m):
            a[nomer_riadka].append(0)
    return a

def postril():
    riad = int(input('Напиши ряд -> '))
    misce = int(input('Вкажи місце -> '))
    riad -= 1
    misce -= 1
    return riad, misce

def stvor_korablia(q):
    q[random.randint(0, 4)][random.randint(0, 4)] = 1
    return q

pole = stvory_pole()                  #  Створюємо пусте поле
pole = stvor_korablia(pole)           #  У випадкову комірку ставимо корабель (один)
for nomer_postrilu in range(10):      #  Реалізуємо 10 пострілів
    riadok, stovpec = postril()       #  просимо у користувача увести рядок і стовпець
    if pole[riadok][stovpec] == 1:    # перевіряємо, якщо 1 то влучив
        print("Вітаю, ти виграв. Мій корабель потоплено :( ")
        break
    else:                             
        print("Мимо. Спробуй ще")
        print(f"Залишилося спроб: {9-nomer_postrilu}")



