class Buerger:
    def __init__(self, name):
        self.name = name
        self.misto = None  # Краще використовувати None, якщо міста немає

    def getBewohnteStadt(self):
        return self.misto
    
    def setBewohnteStadt(self, misto):
        self.misto = misto

    def __str__(self):
        return self.name
    

class Stadt:
    def __init__(self, nazva):
        self.nazva = nazva
        self.meskanci = []

    def einwohnerAnmelden(self, buerge):
        poperednie_misto = buerge.getBewohnteStadt()
        
        if poperednie_misto is not None:
            # Видаляємо громадянина зі списку старого міста
            poperednie_misto.meskanci.remove(buerge)
        
        # Додаємо в нове місто
        self.meskanci.append(buerge)
        buerge.setBewohnteStadt(self) # Передаємо сам об'єкт міста

    def __str__(self):
        m_list = ", ".join([str(i) for i in self.meskanci])
        return f"Місто: {self.nazva}, жителі: {m_list}"

# Тест
buerger1 = Buerger("Max Mueller")
stadt1 = Stadt("Kiel")
stadt2 = Stadt("Hamburg")

stadt1.einwohnerAnmelden(buerger1)
print(stadt1) # Max тут

stadt2.einwohnerAnmelden(buerger1) # Max переїжджає
print(stadt1) # Тут пусто
print(stadt2) # Max тепер тут
