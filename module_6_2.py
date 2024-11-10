class Vehicle:
    _COLOR_VARIANTS = ['BLACK', 'WHITE', 'SILWER', 'RED', 'BROWN']
    def __init__(self, model, engine_power, color, owner):
        self.__model = model
        self.__engine_power = int(engine_power)
        self.__color = color
        self.owner = owner

    def get_model(self):
        print('Модель: ', self.__model)
    def get_engine_power(self):
        print('Мощность двигателя: ', self.__engine_power)
    def get_color(self):
        print('Цвет: ', self.__color)

    def print_info(self):
        print('Модель: ', self.__model)
        print('Мощность двигателя: ', self.__engine_power)
        print('Цвет: ', self.__color)
        print('Владелец: ', self.owner)

    def set_color(self, new_color):
        new_color = new_color.upper()
        for i in range(len(self._COLOR_VARIANTS)):
            if new_color == self._COLOR_VARIANTS[i]:
                self.__color = new_color
                return self.__color
        print(f'Нельзя сменить цвет на {new_color},')
        print(f'Вам доступны следующие цвета: {self._COLOR_VARIANTS}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def get_pass_lim(self):
        print(f'Mаксимальное к-во пассажиров = {self.__PASSENGERS_LIMIT}')

    

v1 = Sedan('BMW X6', 250, 'black', 'Sergo')
print()
print('    *****')
print()
print('get по отдельности:')
v1.get_model()
v1.get_engine_power()
v1.get_color()
print('Owner: ', v1.owner)
v1.get_pass_lim()
print()
print('    Исходное состояние ТС:')
v1.print_info()
v1.get_pass_lim()

print()

print('  Пробуем поменять цвет на Yellow')
v1.set_color('yellow')
print()

print('  Тогда меняем цвет на Red')
v1.set_color('Red')
print()
print('  Так же поменяем владельца')
print()
print('    Итоговое состояние ТС:')
v1.owner = 'Alionka'
v1.print_info()
v1.get_pass_lim()

print()
print('End of lesson')
print('   --------')

