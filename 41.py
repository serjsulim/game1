class televizor:
    def __init__(self):
        self.kanal = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        self.zaraz = 0

    def next(self):
        self.zaraz = (self.zaraz +1) % 30
        print(f'Ви перейшли на канал номер {self.zaraz}')
        print(f'його ім\'я {self.kanal[self.zaraz]}')

    def save(self, name):
        self.kanal[self.zaraz] = name

    def nazva(self):
        print(f'{self.zaraz} канал називається {self.kanal[self.zaraz]}')

    def usi_kanaly(self):
        print(self.kanal)



tv = televizor()
for i in range(30):
    tv.save(input(f"Уведи назву {i} каналу -> "))
    tv.next()
tv.usi_kanaly()

    