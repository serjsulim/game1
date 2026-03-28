slovo = 'sdcmbd'
slovo1 = list(slovo)
while True:
    rez = ''
    text = input(f'Угадай слово із {len(slovo)} букв -> ')
    for nomer_bukvy in range(len(text)):
        if text[nomer_bukvy] == slovo1[nomer_bukvy]: # якщо літера вірна і на своєму місці
            rez = rez +'[' + text[nomer_bukvy] +']'
        elif text[nomer_bukvy] in slovo1:             # якщо літера вірна, але не на місці
            rez = rez +'(' + text[nomer_bukvy] +')'
        else:
            rez += text[nomer_bukvy]                  # інакше виводимо просто його невірну літеру
    if rez.count('[') == 6:                           # Якщо в результаті 6 відкритих квадратних дужок, знач виграв
        print(f'Вітаю! Ти вгадав слово {slovo}')
        break
    else:
        print(rez)
    

