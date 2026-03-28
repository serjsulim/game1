waehrungen = {
    "USD": 1.11, 
    "EUR": 1, 
    "GBP": 0.85, 
    "CHF": 1.06}
while True:
    try:
        suma = int(input("Скільки грошей хочеш поміняти (уведи ціле число) -> "))
        break
    except:
        print('Ти що, дурак?')
while True:
        poc_valuta = input("Яку валюту ти маєш (USD, EUR, GBP, CHF) -> ")
        if poc_valuta in ['USD', 'EUR', 'GBP', "CHF"]:
            break
        else:
            print('Ти що, дурак?')

while True:
        cilova_valuta = input("Яку валюту ти хочеш (USD, EUR, GBP, CHF) -> ")
        if cilova_valuta in ['USD', 'EUR', 'GBP', "CHF"]:
            break
        else:
            print('Ти що, дурак?')

rez = suma * waehrungen[cilova_valuta] / waehrungen[poc_valuta]
print(f'{suma} {poc_valuta} відповідає {rez:.2f} {cilova_valuta}')
