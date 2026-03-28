class Buerger:
    def __init__(self, name):
        self.name = name
        self.misce_reestr = ""

    def getBewohnteStadt(self):
        return self.misce_reestr
    
    def _setStadt(self, misto):
        self.misce_reestr = misto

    def __str__(self):
        return self.name
    
    
class Stadt:
    def __init__(self, name):
        self.name = name
        self.people = []
    
    
    def einwohnerAnmelden(self, name):
        misce = name.getBewohnteStadt()
        #misce.__einwohnerAbmelden(name)
        self.people.append(name)
        name._setStadt(self)

    def __einwohnerAbmelden(self, name):
        if name in self.people:
            self.people.remove(name)
            name._setStadt("")
        
    def __str__(self):
        
        return f"Stadt {self.name}: {", ".join([str(b) for b in self.people])}"


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

print('1', stadt1)
print('2', stadt2)

print(f"\n--- {buerger1} zieht von Kiel nach Hamburg um ---")
stadt2.einwohnerAnmelden(buerger1)

print(stadt1)
print(stadt2)
print('________________________________________')