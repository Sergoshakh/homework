class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        strng = ' Название: ' + self.name + ', количество этажей: ' + str(self.number_of_floors)
        return strng
    def go_to(self, new_floor):
           if new_floor <= 0 or new_floor > self.number_of_floors:
               return print('takogo ne sush')
           else:
               for i in range(1, new_floor+1):
                   print('__ этаж ', i)

    def __eq__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return 'ошибка типа данных!'

    def __lt__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return 'ошибка типа данных!'

    def __le__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return 'ошибка типа данных!'

    def __gt__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return 'ошибка типа данных!'

    def __ge__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return 'ошибка типа данных!'

    def __ne__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return 'ошибка типа данных!'

    def __add__(self, value):
        if isinstance(self, House) and isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            return 'ошибка типа данных!'

    def __sub__(self, value):
        if isinstance(self, House) and isinstance(value, int):
            self.number_of_floors = self.number_of_floors - value
            return self
        else:
            return 'ошибка типа данных!'

    def __mul__(self, value):
        if isinstance(self, House) and isinstance(value, int):
            self.number_of_floors = self.number_of_floors * value
            return self
        else:
            return 'ошибка типа данных!'

    def __truediv__(self, value):
        if isinstance(self, House) and isinstance(value, int):
            self.number_of_floors = self.number_of_floors / value
            return self
        else:
            return 'ошибка типа данных!'

    def __floordiv__(self, value):
        if isinstance(self, House) and isinstance(value, int):
            self.number_of_floors = (self.number_of_floors //value)
            return self
        else:
            return 'ошибка типа данных!'

    def __iadd__(self, value):
        print('работает iadd House+= 10')
        if isinstance(self, House) and isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return 'ошибка типа данных!'

    def __radd__(self, value):
        print('работает radd 200+House')
        if isinstance(self, House) and isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self
        else:
            return 'ошибка типа данных!'


print()
print('    *****')
print()

gk1 = House('ЖК "Эльбрус"', 102)
gk2 = House('ЖК "Акация"', 152)
gk3 = House('ЖК "Гвоздика"', 122)

print(' Наши ЖК:')
print(' ', gk1)
print(' ', gk2)
print(' ', gk3)
print()
print(gk1 == gk3) # False
print(gk1 == 3) # будет ошибка типа данных
print(gk1 > gk3) # False
print(gk1 >= gk3) # False
print(gk1 < gk3) # True
print(gk1 <= gk3) # True
print(gk1 != gk3) # True

print(gk1 + gk3) # будет ошибка типа данных

print(gk1 + 20) # стало 122
print(gk1 == gk3) # теперь Thue
print(gk1 - 5)
print(gk1 * 2)
print(gk1 / 2)
print(gk1 // 3)
print('===')
gk1 += 10
print(gk1)
gk1 = 200 + gk1
print(gk1)

#print('   __str__')
#print(str(gk1))
#print(str(gk2))
#print(str(gk3))
#print('   __len__')
#print('    ',len(gk1))
#print('    ',len(gk2))
#print('    ',len(gk3))
print()
print('End of lesson')
print('   --------')




