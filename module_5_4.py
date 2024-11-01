class House:
    houses_history = []
    deleted_history = []
    def __new__(cls, *args, **kwargs):
        print(' - работает NEW')
        #cls.houses_history.append(args)
        cls.houses_history.append(args[0])
        print('Все построенные ЖК: ', cls.houses_history)
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        
    def __del__(self):
        House.deleted_history.append(self.name)
        return print(f' - {self.name} снесён, но останется в истории')

    def __len__(self):
        return self.number_of_floors


#print()
print('    *****')
#print()

gk1 = House('ЖК "Эльбрус"', 21)
gk2 = House('ЖК "Акация"', 152)
gk3 = House('ЖК "Гвоздика"', 122)
gk4 = House('ЖК "Лео2"', 120)

print()
del gk1
print('Снесённые ЖК: ', House.deleted_history)
print('Все построенные ЖК: ', House.houses_history)

print()
del gk4
print('Снесённые ЖК: ', House.deleted_history)
print('Все построенные ЖК: ', House.houses_history)

print()
print('End of lesson')
print('   --------')
print('Работа программы заканчена, удаляются оставшиеся объекты:')




