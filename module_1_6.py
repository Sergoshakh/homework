my_dict = {'Max': 1945,'Nelly': 1970,'Misha':1955}
print(my_dict)
print(my_dict['Misha'])
print(my_dict.get('Tom','Name "Tom" is missing'))
my_dict.update({'Orruel':1984,
                'Tom': 2000})
print(my_dict)
print(f"Misha's value is {my_dict.pop('Misha')}")
print(my_dict)
print('')
my_set = {1,2,3,4,3,3,2,1,'2',3.3}
print(my_set)
my_set.update({1984,'qwerty'})
print(my_set)
my_set.discard(2)
print(my_set)
print('')
print('РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ ПРОГРАММЫ УРОКА:')
print('')
print(f'Словарь: {my_dict}')
print(f'Значение ключа "Tom": {my_dict['Tom']}')
print(f'Отсутствует ключ "Misha", т.е. его значение: {my_dict.get('Misha')}')
print(f'Убран из словаря ключ "Tom", его значение было равно {my_dict.pop('Tom')}')
print(f'Словарь стал таким: {my_dict}')
print('')
print(f'Множество: {my_set}')
print(f'Удалим 3.3 и добавим список (2,0,9) и число 222')
my_set.discard(3.3)
my_set.update({(2,0,9),222})
print(f'Получим: {my_set}')
print('')
print('End of lesson')
