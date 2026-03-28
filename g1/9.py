def input_integer(text):
    while True:
        try:
            return int(input(text))
        except:
            print("Будь ласка, введіть ціле число.")

def input_float(text):
    while True:
        try:
            return float(input(text))
        except:
            print("Будь ласка, введіть дійсне число.")

w = input_integer('Уведи ціле число -> ')
print(f'Твоє число: {w}')

r = input_float('Уведи дійсне число -> ')
print(f'Твоє число: {r}')   