class Schrittzähler:
    def __init__(self):
        self.steps = 0             # Атрибут для підрахунку кроків

    def addStep(self):
            self.steps += 1       # Збільшує кількість кроків на 1

    def reset(self):
            self.steps = 0       # Обнуляє лічильник кроків

    def showSteps(self):
            print(f"Кількість кроків: {self.steps}")     # Виводить поточну кількість кроків



counter = Schrittzähler() # створюємо змінну
counter.addStep()         # добавляємо крок
counter.addStep()
counter.addStep()
counter.showSteps()   # Виведе кількість кроків
counter.reset()         # обнулить кількість кроків
counter.showSteps()   
