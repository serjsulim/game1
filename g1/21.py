def kilk_sliv(t):
    return len(t.split( ))

def ser_dovg(t):
    a = t.split()
    ser = 0
    for i in a:
        ser += len(i)
    ser = ser / len(a)
    return ser


text = input("Уведи речення -> ")
print(f"Кількість слів: {kilk_sliv(text)}")
print(f'Середня довжина: {ser_dovg(text):.2f}')