def puls(vik):
    p = 165- 0.75*vik
    return p

vik = int(input('Уведи свій вік у роках -> '))
print(f"Оптимальний пульс: {puls(vik):.2f}")