class ZeitreiseMaschine:
    def __init__(self):
       self.zielJahr = 0  # рік призначення
       self.herkunftJahr = 0   # початок руху

    def herkun(self, kudy):
        self.zielJahr = kudy

    def pocatok(self, poc):
        self.herkunftJahr = poc

    def start(self):
        stribok = self.zielJahr - self.herkunftJahr
        if stribok > 0 :
            print(f'Ми стрибнули на {stribok} років уперед')
        elif stribok < 0:
            print(f'Ми стрибнули на {-stribok} років назад')
        else:
            print('Ми не стрибали, бо хтось уводе фігню')

mashina = ZeitreiseMaschine()
mashina.herkun(int(input('Куди? ')))
mashina.pocatok(int(input('Звідки? ')))
mashina.start()