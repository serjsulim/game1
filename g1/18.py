def suma (t):
    summ = 0
    for i in range(len(t)):
        summ += t[i]
    ser = summ/ len(t)
    return ser 


produktpreise = [100, 150, 200, 250, 300, 500, 20, 30, 80, 12, 8, 23, 45]
print(f"Середня ціна становить : {suma(produktpreise):.2f} євро")