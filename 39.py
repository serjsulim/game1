class Warteschlange:
    def __init__(self):      # створюємо внутрішню змінну черга
        self.therga = []     # і кажемо, що це пустий список
        

    def ankommen(self, name):     # метод, що додаватиме людину в кінець списку
        self.therga.append(name)  # у внутрішню змінну черга у кінець додаємо уведене ім'я

    def verlassen(self):               # метод, що виводитиме на екран першого з черги
        print(self.therga[0])          #
        self.therga.pop(0)             # і видаляє його з черги

    def ausgabe(self):                    # метод, що виводить на екран усю чергу
        print(self.therga)      

w = Warteschlange()      
w.ausgabe()

w.ankommen("Alina")
w.ankommen("Bernd")
w.ankommen("Christoph")
w.ausgabe()
w.verlassen()
w.verlassen()
w.verlassen()
w.ausgabe()