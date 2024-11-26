def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            print(f' - ВНИМАНИЕ! Элемент ({i}) имеет некорректный тип данных для операции сложения чисел, исключение: /{exc}/, пропускаем этот элемент')
            incorrect_data += 1
    return (result, incorrect_data)
        
def calculate_average(numbers):
    try:
        res_sum = personal_sum(numbers)
    except TypeError as exc:
        print(f' - ВНИМАНИЕ! Введённые данные имеют некорректный тип, исключение: /{exc}/, завершаем программу')
        print('Среднее арифметическое = ', end='')
        return None
    try:
        avr = res_sum[0] / (len(numbers) - res_sum[1])
    except ZeroDivisionError as exc1:
        print(f' - ВНИМАНИЕ! Происходит деление на ноль, исключение: /{exc1}/, завершаем программу')
        print('Среднее арифметическое = ', end='')
        return 0
    print('Среднее арифметическое = ', end='')
    return avr

#print('сумма введённых чисел =', final_res[1])
#print('количество некорректных данных =', final_res[2])
#print('среднее арифметическое введённых чисел =', final_res[0])
print(calculate_average('1, 2, 3'))
print()
print(calculate_average([1, "Строка", 3, "Ещё Строка"]))
print()
print(calculate_average(561))
print()
print(calculate_average([42, 15, 36, 13]))