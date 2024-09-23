immutable_var = 1, 'a', True, [2,3,4,5]
print(immutable_var)
# immutable_var[0] = 2
# значения кортежа неизменяемые, в отличии от значений списков
immutable_var[3][1] = 2
print(immutable_var)
str0 = '1966', False
imv = immutable_var + str0
print(imv)
print(imv[1::2])
print(type(immutable_var))
mutable_list = [1, 'a', True, [2,3,4,5]]
print(mutable_list)
mutable_list[0] = 2
print(mutable_list)
mutable_list.append('добавка')
print(type(mutable_list))
print(mutable_list)
print('')
print('ОТВЕТ ПО ЗАДАНИЮ:')
print('')
print(f'immutable tuple: {imv}')
print(f'mutable list: {mutable_list}')