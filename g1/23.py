text = input('Уведи зашифрований текст -> ').upper()
key = int(input('Уведи ключ -> '))
abetka = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rezult = ''
for i in range(len(text)):
    nomer = abetka.index(text[i])
    new_nomer = (nomer + key + 1) % 26
    rezult += abetka[new_nomer]
print(f"Розшифроване повідомлення: {rezult.capitalize()}")