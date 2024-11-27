class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin):
        if isinstance(vin, int) == False:
            raise IncorrectVinNumber('некорректный тип VIN', 'тип должен быть (int)')
        if vin < 1000000 or vin > 9999999:
            raise IncorrectVinNumber('номер VIN вне корректного диапазона',
                                     'диапазон должен быть в пределах от 1000000 до 9999999')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) == False:
            raise IncorrectCarNumbers('некорректный тип данных для номеров ', 'тип должен быть (str)')
        if len(numbers) != 6 :
            raise IncorrectCarNumbers('неверная длина номера ', 'длина номера должна быть = 6')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

class IncorrectCarNumbers(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


try:
    first = Car('Ford Focus',  1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(f'сообщение об ошибке: / {exc.message} /; дополнительная информация: {exc.extra_info}')
except IncorrectCarNumbers as exc1:
    print(f'сообщение об ошибке: / {exc1.message} /; дополнительная информация: {exc1.extra_info}')
else:
    print(f'{first.model} успешно создан')

try:
    first = Car('Hunday Solaris', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(f'сообщение об ошибке: / {exc.message} /; дополнительная информация: {exc.extra_info}')
except IncorrectCarNumbers as exc1:
    print(f'сообщение об ошибке: / {exc1.message} /; дополнительная информация: {exc1.extra_info}')
else:
    print(f'{first.model} успешно создан')

try:
    first = Car('Opel Astra', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(f'сообщение об ошибке: / {exc.message} /; дополнительная информация: {exc.extra_info}')
except IncorrectCarNumbers as exc1:
    print(f'сообщение об ошибке: / {exc1.message} /; дополнительная информация: {exc1.extra_info}')
else:
    print(f'{first.model} успешно создан')

