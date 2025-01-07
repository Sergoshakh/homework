import sys
from inspect import ismethod
import inspect


class My_Class:
    def __init__(self):
        self.attribute_2 = None
        self.attribute_1 = 27

    def my_method1(self, value):
        self.attribute_2 = value

    def my_method2(self):
        print(self.attribute_1 * self.attribute_2)

def introspection_info(obj):
    method = []
    attributes = []
    for item in dir(obj):
        if callable(getattr(obj, item)):
            method.append(item)
        else:
            attributes.append(item)
    obj_module = inspect.getmodule(obj)

    print('Тип объекта:', type(obj))
    print(f'Объект вызываемый - {callable(obj)}')
    print(f'Методы объекта: {method}')
    print(f'Атрибуты объекта: {attributes}')
    print(f'Объект находится в {obj_module}' )
    print(f'\n - ОС - "{sys.platform}"')
    print(f' - Версия Python - {sys.version}\n')


my_object = My_Class()

print(f'\n *** пример интроспекции объекта "my_object" класса "My_Class" ***\n')
introspection_info(my_object)
