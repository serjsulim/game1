def berechne_anhalteweg(geschwindigkeit):
    reaktionsweg = geschwindigkeit / 10 * 3
    bremsweg = (geschwindigkeit / 10) * (geschwindigkeit / 10)
    anhalteweg = reaktionsweg + bremsweg
    return anhalteweg

geschwindigkeit = float(input('Уведи швидкість -> '))
anhalteweg = berechne_anhalteweg(geschwindigkeit)
print(f'Гальмівний шлях при швидкості {geschwindigkeit} км/год: становить {anhalteweg:.2f} м')
