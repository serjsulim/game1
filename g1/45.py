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

class VorlesungOnline(Vorlesung):
    def __init__(self, zoom):
        super().__init__()
        self.zoom = zoom
        
    
lekcia3 = VorlesungOnline(zoom="https//2121312")
link = getattr(lekcia3, "zoom")
print(link)

setattr(lekcia3, "zoom", "asmdasdkapokpodk" )
link = getattr(lekcia3, "zoom")
print(link)


