from time import sleep


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self):
           new_floor = int(input('На какой этаж поедем? : '))
           if new_floor <= 0 or new_floor > self.number_of_floors:
               return print('Ошибка! Такого этажа не существует')
           else:
               for i in range(1, new_floor+1):
                   sleep(0.5)
                   print('__ этаж ', i)



print()
print('    ***')
print()
gke = House('ЖК "Эльбрус"', 21)
print(gke.name, gke.number_of_floors)
gke.go_to()
print('_готово!')
sleep(0.5)
print()
print('   --------')
print()
dvk = House('Домик в коттетже', 1)
print(dvk.name, dvk.number_of_floors)
dvk.go_to()
print('В домике только один этаж...')
print()
sleep(0.5)
print('End of lesson')
print('   --------')
