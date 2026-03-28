class Buch:
    def __init__(self, titel, autor = '', isbn = ''):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f'Назва: {self.titel}; автор: {self.autor}'
   
class Bücherregal:
    def __init__(self):
        self.spisok = []

    def buchHinzufügen(self, book):                 # додати книгу на полицю
        self.spisok.append(book)
        print(f"Книгу {book} додано на полицю")
    def buchEntfernen(self, book):                  # видалити книгу з полиці
        if book in self.spisok:
            self.spisok.remove(book)
            print(f"Книгу {book} видалено з полиці")
        else:
            print(f'Книги {book} на полиці немає')
    def alleBücherAnzeigen(self):                  # показати всі книги
        if self.spisok == []:
            print('полиця пуста')
        else:
            print('Список усіх книг')
            for book in self.spisok:
                print(book)

    def sucheBuch(self, name):              #Пошук
        for book in self.spisok:
            if book.titel == name or book.autor == name:
                print(f'Книга {book} знайдена')
                return
        print(f'Книга {name} не знайдена')




    

b1 = Buch('Робінзон Крузо', "Даніель Дефо")
b2 = Buch('Гаррі Потер', 'Джоан Роулінг')
b3 = Buch('Відьмак', 'Анджей Сапковський')
b4 = Buch('Математика', 'Істер')

polka1 = Bücherregal()      

polka1.buchHinzufügen(b1)     # Додаємо по черзі 3 книги
polka1.buchHinzufügen(b2)
polka1.buchHinzufügen(b3)

polka1.alleBücherAnzeigen()   # показати всі

polka1.buchEntfernen(b1)
print('++++++++++++++++++++++++++++++++++++')

polka1.alleBücherAnzeigen()
polka1.buchEntfernen(b4)

print('------------------------------------------')

