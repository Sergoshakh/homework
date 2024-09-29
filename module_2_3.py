my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
y = 0
x = 1
len_ = len(my_list)
while y < len_:
    x = int(my_list[y])
    y += 1
    if x < 0:
        print('Встретилось отрицательное значение, завершаем вывод')
        break
    if x > 0:
        print(x)
    else:
        continue
print('')
print('End of lesson')
