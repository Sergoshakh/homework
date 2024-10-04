list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
keys_i = []
keys = []
dict_result = {}
for i in range(18):
    for j in range(20):
        if list_[i] == list2[j]:
            keys_i.append(keys)
            dict_result.update({list_[i]: keys_i[i]})
            keys = []
            break
        for k in range(20):
            if list_[i] < (list2[k] + list2[j]):
                break
            else:
                if k <= j:
                    continue
                else:
                    if list_[i] % (list2[j] + list2[k]) == 0:
                    #if list_[i] % (list2[j] + list2[k]) == 0 and list_[i] // (list2[j] + list2[k]) == 1:
                        keys.append(list2[j])
                        keys.append(list2[k])
print('')


def enter_int():
    n = int(input('Введите число от "3" до "20": '))
    while n < 3 or n > 20:
        print('Неверный ввод, введёное число выходит за рамки заданного диапазона!')
        n = int(input('повторите ввод: '))
        print('')
    return n


n = enter_int()
print(f'Пароль для числа {n} будет  {dict_result[n]}')
print('')
ans = input('Хотите повторить? ( Y / any key )')
print('')
while ans == 'y':
    n = enter_int()
    print(f'Пароль для числа {n} будет {dict_result[n]}')
    print('')
    ans = input('Хотите повторить? ( Y / any key )')
print('')
print('End of lesson')
