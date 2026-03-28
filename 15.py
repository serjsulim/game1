ocinka = float(input('Оцінка -- > '))
othi = int(input("Колір очей -> "))
zatciska = int(input('Зачіска -> '))
pogoda = int(input('Погода -> '))

if othi == 1 and zatciska == 1:
    ocinka += ocinka * 0.1
if othi == 1 and zatciska == 0:
    ocinka -= ocinka * 0.1
if othi == 0 and zatciska == 1:
    ocinka -= ocinka * 0.1
if othi == 0 and zatciska == 0:
    ocinka += ocinka * 0.1
if pogoda == 1:
    ocinka -= 1
ocinka = round(ocinka*2)/2
print(f'Оцінка {ocinka:.1f}')