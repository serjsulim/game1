class Buerger:
    def __init__(self, name):
        self.name = name
        self.__bewohnte_stadt = None  # Приватне поле для зберігання поточного міста

    def getBewohnteStadt(self):
        """Повертає об'єкт міста, де зараз зареєстрований громадянин."""
        return self.__bewohnte_stadt

    def _setStadt(self, stadt):
        """Технічний метод для оновлення посилання на місто (не для користувача)."""
        self.__bewohnte_stadt = stadt

    

class Stadt:
    def __init__(self, name):
        self.name = name
        self.__einwohner_liste = []  # Список мешканців міста

    def einwohnerAnmelden(self, buerger):
        """Публічний метод для реєстрації мешканця."""
        # 1. Дізнаємося, де людина живе зараз
        alte_stadt = buerger.getBewohnteStadt()

        # 2. Якщо людина вже десь живе і це не це саме місто
        if alte_stadt and alte_stadt != self:
            # Нове місто саме ініціює зняття з реєстрації у старого міста
            alte_stadt._einwohnerAbmelden(buerger)
            print(f"--- [Система] {buerger} автоматично знятий з обліку в м. {alte_stadt.name} ---")

        # 3. Реєструємо у себе, якщо ще не зареєстрований
        if buerger not in self.__einwohner_liste:
            self.__einwohner_liste.append(buerger)
            buerger._setStadt(self)
            print(f"--- [Система] {buerger} успішно зареєстрований у м. {self.name} ---")

    def _einwohnerAbmelden(self, buerger):
        """
        Непублічний метод. 
        За логікою задачі, його не має викликати користувач вручну, 
        його викликає 'нове' місто.
        """
        if buerger in self.__einwohner_liste:
            self.__einwohner_liste.remove(buerger)
            buerger._setStadt(None)

    def __str__(self):
        return f"Місто {self.name}, мешканці: {self.__einwohner_liste}"


# --- Демонстрація роботи програми ---

# Створюємо громадян
buerger1 = Buerger("Max Mueller")
buerger2 = Buerger("Sarah Maier")

# Створюємо міста
kiel = Stadt("Kiel")
hamburg = Stadt("Hamburg")

print(f"Початковий стан:")
print(kiel)
print(hamburg)

print(f"\n1. Реєструємо {buerger1} у місті Kiel...")
kiel.einwohnerAnmelden(buerger1)
print(kiel)

print(f"\n2. Тепер {buerger1} вирішує переїхати до Hamburg...")
# Hamburg сам звернеться до Kiel, щоб виписати громадянина
hamburg.einwohnerAnmelden(buerger1)

print(f"\nФінальний стан:")
print(f"Kiel після переїзду: {kiel}")
print(f"Hamburg після переїзду: {hamburg}")