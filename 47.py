class Fisch:
    def __init__(self, art = '', farbe = '', groesse = ''):
        self.art = art
        self.farbe = farbe
        self.groesse = groesse

class Aquarium:
    def __init__(self, rybky = []):
        self.rybky = rybky

    def add_rybka(self, ryba):
        self.rybky.append(ryba)

    def del_rybka(self, ryba):
        self.rybky.remove(ryba)

    def info(self):
        for i in self.rybky:
            print(f'вид: {i.art}, колір: {i.farbe}, розмір: {i.groesse}')

r1 = Fisch('короп', 'синій', 'великий')
r2 = Fisch('карасик', 'зелений', 'маленький')
r3 = Fisch("скалярія", 'рожева', 'маленька')
a1 = Aquarium()
a1.add_rybka(r1)
a1.add_rybka(r2)
a1.add_rybka(r3)
a1.info()
print('___________')
a1.del_rybka(r1)
a1.info()
