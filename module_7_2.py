import io
from pprint import pprint

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

dic = {}

file_name = 'text'

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
 #   ln = (len(strings))
    k = 1
    num_b = 0
    for i in strings:
        num_b = file.tell()
        dic[k, num_b] = i
        k += 1
        file.write(i)
        file.write('\n')
    file.close()
    return dic

result = custom_write('text.txt', info)

print()
print('    *****')
print()

for elem in result.items():
    print(elem)
print()
print('End of lesson')
print('   --------')
