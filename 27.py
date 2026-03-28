warenlager = {
    'Butter': 1.90,
    'Brot': 2.30,
    'Schokolade': 1.50,
    'Apfel': 4.20}

vartist = 0
but  = int(input('Скільки бутерів ти хочеш -> '))
br  = int(input('Скільки хліба ти хочеш -> '))
sc = int(input('Скільки шоколадок ти хочеш -> '))
ap = int(input('Скільки яблучок ти хочеш -> '))
vartist = warenlager['Apfel'] * ap + warenlager['Brot'] * br + warenlager['Schokolade'] * sc + warenlager['Butter'] * but
print(f"Вартість твого замовлення {vartist:.2f} євро")