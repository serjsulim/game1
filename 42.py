class Vorlesung:
    def __init__(self):
        self.titel = ""
        self.studierende = []

    def schreibeEin(self, name):
        self.studierende.append(name)

    def schreibeAus(self, name):
        self.studierende.remove(name)

    def getAnzahlStudierende(self):
        print(len(self.studierende))

    def getStudierende(self):
        a = sorted(self.studierende)
        print(a)

    def str1(self, nazva):
        self.titel = nazva



lekcia1 = Vorlesung()
lekcia2 = Vorlesung()
lekcia1.schreibeEin('Alina')
lekcia1.schreibeEin('Zet')
lekcia1.schreibeEin('Vadim')
lekcia1.schreibeEin('Anna')
lekcia2.schreibeEin('Egor')
lekcia2.schreibeEin('Masha')
lekcia2.schreibeEin('Vova')
lekcia1.getStudierende()
