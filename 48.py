class Room:
    def __init__(self, nomer, status = True ):
        self.nomer = nomer
        self.status = status

    def isAvailable(self):       # перевіряє, чи номер вільний
        if self.status == True:
            return True
        else:
            return False

    def setAvailable(self, nomer ):
        self.status = not self.status

    def getNumber(self):
        return self.nomer

class Hotel:
    def __init__(self, name, spysok_nomeriv):
        self.name = name
        self.spysok_nomeriv = spysok_nomeriv

    def checkIn(self):
        for i in self.spysok_nomeriv:
            if i.isAvailable(self):
                return i.nomer
    


rooms = []
rooms.append(Room(101))
rooms.append(Room(102))
rooms.append(Room(103))
rooms.append(Room(201))
rooms.append(Room(202))
rooms.append(Room(203))

hotel = Hotel("Kieler Förde", rooms)

hotel.checkIn()
hotel.checkIn()
hotel.checkIn()
hotel.checkOut(102)
hotel.checkIn()
hotel.checkIn()
hotel.checkOut(203)

"""
Очікуваний вивід у консолі:
Zimmer 101 wurde gebucht.
Zimmer 102 wurde gebucht.
Zimmer 103 wurde gebucht.
Zimmer 102 wurde ausgecheckt.
Zimmer 102 wurde gebucht.
Zimmer 201 wurde gebucht.
Zimmernummer 203 war nicht gebucht."""