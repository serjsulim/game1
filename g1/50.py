class Buerger:
    def __init__(self, name):
        self.name = name
        self.misto = None      # краще None замість ''

    def getBewohnteStadt(self):    # повертає назву міста, де зареєстрований
        return self.misto
    
    def setBewohnteStadt(self, misto):   #міняє у громадянина місто на нове
        self.misto = misto

    def __str__(self):             # для правильного виводу на екран
        return self.name
    

class Stadt:
    def __init__(self, nazva):
        self.nazva = nazva
        self.meskanci = []

    def einwohnerAnmelden(self, buerge):           # зареєструвати мешканця
        misce = buerge.getBewohnteStadt()          
        if misce != None:
            misce._einwohnerAbmelden(buerge)  ## використовувати ОДНЕ підкреслення
        self.meskanci.append(buerge)
        buerge.setBewohnteStadt(self) # !!!!!!! помилка була тут, 
                                      # передавали назву міста а треба весь об'єкт

    def _einwohnerAbmelden(self, buerge):  # виписати мешканця            
        if buerge in self.meskanci:
            self.meskanci.remove(buerge)
        buerge.setBewohnteStadt(None)

    def __str__(self):
        return f'Місто: {self.nazva}; жителі {', '.join([str(i) for i in self.meskanci])}'


    
        

buerger1 = Buerger("Max Mueller")
buerger2 = Buerger("Bernd Walter")
buerger3 = Buerger("Sarah Maier")
buerger4 = Buerger("Kim Bauer")

stadt1 = Stadt("Kiel")
stadt2 = Stadt("Hamburg")

print("Die Bürger melden sich an...")

stadt1.einwohnerAnmelden(buerger1)
stadt1.einwohnerAnmelden(buerger2)
stadt2.einwohnerAnmelden(buerger3)
stadt2.einwohnerAnmelden(buerger4)

print(stadt1)
print(stadt2)

stadt2.einwohnerAnmelden(buerger1)

print(stadt1)
print(stadt2)
