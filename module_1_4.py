my_string = input('введите какую-нибудь фигню: ')
print('Введённая фигня:',my_string)
dlina = len(my_string)
str_dlina = str(dlina)
end_chisla = int(str_dlina[-1])
if dlina >= 5 and dlina<=20:
    slovo = ' символов'
elif end_chisla == 1:
    slovo = ' символ'
elif (end_chisla == 2 or end_chisla == 3 or end_chisla == 4):
    slovo = ' символа'
else: slovo = ' символов'
print(f'длина строки введённой фигни составила {dlina}{slovo}')
print(f'Эта строка в верхнем регистре: {my_string.upper()}')
print(f'Эта строка в нижнем регистре: {my_string.lower()}')
print(f'Эта строка без пробелов: {my_string.replace(" ","")}')
print(f'Первый символ этой строки: {my_string[0]}')
print(f'Последний символ этой строки: {my_string[-1]}')
print('End of lesson')
