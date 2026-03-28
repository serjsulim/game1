def godyny(hv):
    doba = hv //(24*60)
    hv = hv - doba*24*60
    god = hv // 60
    hvyl = hv % 60
    return doba, god, hvyl

hv = int(input('Уведи кількість хвилин -> '))
doba, god, hvyl = godyny(hv)
print(f"{doba} діб, {god} годин і {hvyl} хвилин")
