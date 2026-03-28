def nova_cina(poch_cina, vids_znyzky):
    nova = poch_cina - (poch_cina * vids_znyzky / 100)
    return nova

poch_cina = float(input('Уведи початкову ціну -> '))
vids_znyzky = float(input('Уведи відсотки знижки -> '))
print(f'Нова ціна після знижки: {nova_cina(poch_cina, vids_znyzky):.2f} євро')  

    