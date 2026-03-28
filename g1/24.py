alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input("Уведи текст для шифрування -> ").upper()
key = int(input('Уведи ключ -> '))
rez = ''
for i in range(len(text)):
    nomer = alfavit.index(text[i])
    rez += alfavit[(nomer + key + 1) % 26]
print(f'Зашифрований текст: {rez.capitalize()}')