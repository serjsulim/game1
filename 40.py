class Sparschwein:
    def __init__(self):
        self.money = 0

    def einzahlen(self, groshi):
        self.money += groshi
        print(f'{groshi} успішно зараховано')

    def abheben(self, groshi):
        if self.money >= groshi:
            self.money -= groshi
            print(f'{groshi} успішно знято')
        else:
            print('Не вистачає коштів')

    def zeige_geldbestand(self):
        print(self.money)

rosa_sparschwein = Sparschwein()
rosa_sparschwein.einzahlen(120)
rosa_sparschwein.abheben(90)
rosa_sparschwein.abheben(50)
rosa_sparschwein.zeige_geldbestand()
