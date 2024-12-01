first = ['strings', 'student', 'computers']
second = ['строка', 'урбан', 'компьютер']

zp = zip(first, second)
first_result = (len(x[0]) - len(x[1])  for x in zp if (len(x[0]) - len(x[1])) != 0)
print(list(first_result))

lt = first + second
result = (len(x) == len(y) for x in first for y in second)

result = list(result)

second_result = []
for i in range(0, len(result), 4):
    second_result.append(result[i])

print(list(second_result))
