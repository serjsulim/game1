bestellungen = ["Apfel:19:2.5", "Banane:5:0.8", "Avocado:2:1.5", "Birne:4:0.7"]
sum = 0
for i in bestellungen:
    rez = i.split(':')
    sum += int(rez[1]) * float(rez[2])
print(f"Suma = {sum}")

