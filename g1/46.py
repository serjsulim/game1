class Tier:
    def __init__(self, vyd = '', name = ''):
        self.vyd = vyd
        self.name = name

    def laut_geben(self):
        print('RRRRRRRR')


class Hund(Tier):
 
    def laut_geben(self):
        print('Wuff')

class Katze(Tier):
 
    def laut_geben(self):
        print('Miau')



tvaryna1 = Tier("крокодил", "Вася")
tvaryna2 = Hund("собака", 'Тузик')
tvaryna3 = Katze('Кіт', "Мурка")
tvaryna1.laut_geben()
tvaryna2.laut_geben()
tvaryna3.laut_geben()

