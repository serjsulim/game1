gehalt_liste = [3500.5, 4200.75, 3100.25, 2900.10]
gehalt_bonus = []
for i in gehalt_liste:
    if i < 3000:
        gehalt_bonus.append(i + i* 0.1 )
    else:
        gehalt_bonus.append(i + i* 0.05 )
gehalt_bonus.sort()            # сортуємо список зарплат з бонусами    
for i in gehalt_bonus:
    print(f"{i:.2f} e")
