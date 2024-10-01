def get_matrix(n, m, value):
    matrix = []
    if n <= 0:
        return matrix
    if m <= 0:
        return matrix
    str_matrix = []
    for j in range(m):
        str_matrix.append(value)
    for i in range(n):
        matrix.append(str_matrix)
    return matrix
n = int(input('Введите количество строк в матрице: '))
m = int(input('Введите количество столбцов: '))
value = int(input('Введите значения в матрице: '))
result = get_matrix(n, m, value)
print('-------------------------------------')
print('Результат: ', result)
print('')
print('End of lesson')