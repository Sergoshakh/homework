print('Введите три целых числа:')
first = int(input(' - первое: '))
second = int(input(' - второе: '))
third = int(input(' - третье: '))
if first == second and first == third:
    print(f'Три одинаковых числа {first}')
elif first == second or first == third:
    print(f'Два одинаковых числа {first}')
elif second == third:
    print(f'Два одинаковых числа {second}')
else:
    print(f'Одинаковых чисел нет')
print('')
print('End of lesson')