class Buerger:
    def __init__(self, name):
        self.name = name
        self.__stadt = None  # Місто, де зараз прописаний

    def getBewohnteStadt(self):
        return self.__stadt

    def _setStadt(self, stadt):
        self.__stadt = stadt

    def __str__(self):
        return self.name


class Stadt:
    def __init__(self, name):
        self.name = name
        self.__einwohner = []

    def einwohnerAnmelden(self, buerger):
        # 1. Перевіряємо, чи є стара прописка
        alte_stadt = buerger.getBewohnteStadt()
        
        if alte_stadt:
            # 2. Викликаємо приватний метод старого міста для зняття з реєстрації
            # В Python доступ до __ методів іншого екземпляра того ж класу можливий
            alte_stadt._Stadt__einwohnerAbmelden(buerger)
        
        # 3. Реєструємо в новому місті
        if buerger not in self.__einwohner:
            self.__einwohner.append(buerger)
            buerger._setStadt(self)

    def __einwohnerAbmelden(self, buerger):
        if buerger in self.__einwohner:
            self.__einwohner.remove(buerger)
            buerger._setStadt(None)

    def __str__(self):
        einwohner_liste = ", ".join([str(b) for b in self.__einwohner])
        return f"Stadt {self.name}: [{einwohner_liste}]"


# --- Тестування ---
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

print(f"\n--- {buerger1} zieht von Kiel nach Hamburg um ---")
stadt2.einwohnerAnmelden(buerger1)

print(stadt1)
print(stadt2)
