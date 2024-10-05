def count_calls():
    global calls
    calls += 1
    
def string_info(str_):
    count_calls()
    list_ = (len(str_), str_.upper(), str_.lower())
    return list_

def is_contains(str_, list_to_search):
    count_calls()
    str_ = str_.lower()
#    print(str_)
    len_=len(list_to_search)
#    print(len_)
    for i in range(len_):
        len_i = len(list_to_search[i])
        for j in range(len_i):
            list_to_search[i] = list_to_search[i].lower()
#    print(list_to_search)
    return str_ in list_to_search

print('')

calls = 0
ans = 0

while True:
    print('')
    str_ = input('Введите строку для проверки функции "string_info": ')
    list_ = string_info(str_)
    print(f'результат работы функции "string_info": {list_}')
    print('')
    print(f'набор строк для сравнения: "uRbaN", "QWErty", "sddgK"')
    str_ = input('C учётом вышеназванного набора строк введите строку для проверки функции "is_contains": ')
    print('')
    if is_contains(str_, ['uRbaN', 'QWErty', 'sddgK']) == True:
        print(f'строка "{str_}" ,без учёта регистра ВХОДИТ в набор строк для сравнения')
    else:
        print(f'строка "{str_}" НЕ ВХОДИТ в набор строк для сравнения')
    print('')
    ans = input('Повторить? ( Y / any key) ')
    if ans == 'y' or ans == 'Y':
        continue
    else:
        break
    print('')

print('')
print(f'Количество вызовов вызшеназванных функций - {calls}')
print('')
print('End of lesson')