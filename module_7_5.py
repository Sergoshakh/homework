import os
import time

#directory = os.path.abspath('first')
#directory = "."
directory = os.getcwd()

print()
print('    *****')
print()

print(directory)

#os.chdir(directory)
print('текущая дирктория', os.getcwd())
print()

for root, dirs, files in os.walk(directory):
    for file in files:
        print(f'Oбнаружен файл: {file}')
        path = os.path.join(root)
        print('Путь: ', path)
        os.chdir(path)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime('%d.%m.%Y.%H.%M', time.localtime(filetime))
        print(f'Время изменения: {formatted_time}')
        print(f'Размер: {os.path.getsize(file)} байт')
        parent_dir = os.path.dirname(path)
        print(f'Родительская директория: {parent_dir}')
        print()
print('End of lesson')
print('   --------')
