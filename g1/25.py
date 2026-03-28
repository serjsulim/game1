wochen_preise = [10, 12, 15, 9, 8, 14, 13, 11, 15, 16]
schwellenwert = int(input('Уведи граничне значення -> '))
dniv = 0
for tcina_sogodni in wochen_preise:
    if tcina_sogodni > schwellenwert:
        dniv += 1
print(f"Кількість днів {dniv}")