import threading
import time
from threading import main_thread
from time import sleep

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='UTF-8')
    for i in range(word_count):
        line = 'Какое-то слово № ' + str(i + 1) + '\n'
        file.write(line)
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
job_time = round(end_time - start_time, 3)
print('Работа потоков = ', job_time)

start_time = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time = time.time()
job_time = round(end_time - start_time, 3)
print('Работа потоков = ', job_time)
