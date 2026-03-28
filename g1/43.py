class Rectangle:
    def __init__(self, dovz, shir):
        self.dovzina = dovz
        self.hirina = shir

    def plosca(self):
        print(f"Площа прямокутника {self.dovzina * self.hirina}")

pr1 = Rectangle(10, 5)
pr1.plosca()
pr2= Rectangle(200, 20)
pr2.plosca()
