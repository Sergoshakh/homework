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

#print()
print('    *****')
#print()

gk1 = House('ЖК "Эльбрус"', 21)
gk2 = House('ЖК "Акация"', 152)
gk3 = House('ЖК "Гвоздика"', 122)

print('   __str__')
print(str(gk1))
print(str(gk2))
print(str(gk3))
#print()
print('   __len__')
print('    ',len(gk1))
print('    ',len(gk2))
print('    ',len(gk3))
print('End of lesson')
print('   --------')




