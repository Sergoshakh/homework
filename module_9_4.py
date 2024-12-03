from random import choice
#from pprint import pprint
#import io


first = 'Мама мыла раму'
second = 'Рамена мало было'
first.replace(' ', '')
second.replace(' ', '')
print(list(map(lambda x, y: x == y, first, second)))



def get_advanced_writer(file_name):
    file = open(file_name, 'w', encoding='utf-8')
    def write_ewerything(*data_set):
        for elem in data_set:
            file.write(str(elem))
            file.write('\n')
        file.close()
    return write_ewerything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



class MysticBall:
    words = []
    def __init__(self, *args):
        self.words = args
    def __call__(self):
        result_word = choice(self.words)
        return result_word

first_ball = MysticBall('да', 'нет', 'наверное', 'ну', 'нафиг')
print(first_ball())
print(first_ball())
print(first_ball())
