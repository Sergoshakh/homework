def print_params(a = 99, b = 'stroka', c = True):
    print(a, b, c)

print('')
print('    * * *')
print('')
print('    1. Функция с параметрами по умолчанию.')
print('')
print("  Вызов функции с параметрами по умолчанию a = 99, b = 'stroka', c = True :")
print_params()
print('')
print('  Вызов функции с изменённым параметрам "b"=25 :')
print_params(b = 25)
print('')
print('  Вызов функции с изменённым параметрам "c"=[1,2,3] :')
print_params(c = [1, 2, 3])
print('')
print('  Вызов функции с изменённымb параметрам "a"=a25 и "b"=3 :')
print_params('a25', 3)
print('')
print('  Вызов функции с изменённым параметрам "a"=a25, "b"=25 и "c"=33 :')
print_params('a25', 3, 33)
print('')
print('    2. Распаковка параметров.')
values_list = [False, ['b21', 'b22', 23], {'da' : 11, 'db' : 12, 'dc' : 13}]
values_dict = {'a' : 'one', 'b' : 'two', 'c' : 'three'}
print('')
print("  Вызов функции с распакованным списком value_list=[False, ['b21', 'b22', 23], {'da' : 11, 'db' : 12, 'dc' : 13}]:")
print_params(*values_list)
print('')
print("  Вызов функции с распакованными значениями словаря {'a' : 'one', 'b' : 'two', 'c' : 'three'} :")
print_params(**values_dict)
print('')
values_list_2 = [['b21', 'b22', 23], {'da' : 11, 'db' : 12, 'dc' : 13}]
print('    2. Распаковка + отдельные параметры.')
print('')
print("  Вызов функции с распакованным списком values_list_2=[['b21', 'b22', 23], {'da' : 11, 'db' : 12, 'dc' : 13}] и значением 'c'=42 :")
print_params(*values_list_2, 42)
print('')
print('End of lesson')