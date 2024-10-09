def get_multiplied_digits(number):
    number = int(number) # убираем нули если number начинается с них
    str_number = str(number)
    first = int(str_number[0])


    if first == 0: # Нейтрализуем нули в конце числа number
        return 1

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print('')
print('    * * *')
print('')

ans = 'y'
while ans == 'y' or ans == 'Y':
    num = input('Введите число больше "0" : ')
    if int(num) == 0:
        print('Неверный ввод, число = 0 !')
    else:
        print(f'Произведение цифр числа {num} равно {get_multiplied_digits(num)}')
    print('')
    ans = input('Повторить? ( Y / any key) ')
    print('')
print('End of lesson')
