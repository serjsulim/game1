

oborot =[] 
for i in range(1,13):
    oborot.append(int(input(f"Будь ласка, уведіть оборот за місяць {i}: ")))

print(f"Найвищий оборот року: {max(oborot):.2f} євро")
print(f"Найменший оборот року: {min(oborot):.2f} євро")
serednij_oborot = 0
for i in range(12):
    serednij_oborot += oborot[i]
serednij_oborot = serednij_oborot / 12
print(f"Середній оборот року: {serednij_oborot:.2f} євро")