import io
from pprint import pprint

class Words_Finder:
    def __init__(self, *args):
        self.file_names = args
        self.all_words = {}

    def get_all_words(self):
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                a = ''
                print()
                print(f'   Содержание файла {name}:')
                for line in file:
                    line = line.lower()
                    k = -2
                    for i in line:
                        k += 1
                        if i == ',' or i == '.' or i == '=' or  i == '!' or i == '?' or i == ';' or i == ':':
                            continue
                        else:
                             if i == '-' and line[k] == ' ' and k >= 0:
                                 continue
                             a += i
                    print(line, end='')
                line = a.split()
                self.all_words[name] = line

    def find(self, word):
        for name, words in self.all_words.items():
            for i in range(len(words)):
                if words[i] == word:
                    print(f' В файле "{name}" слово "{words[i]}" впервые встречается {i+1}-м по счёту словом')


    def count(self, word):
        for name, words in self.all_words.items():
            k = 0
            for i in range(len(words)):
                if words[i] == word:
                    k += 1
            print(f' В файле "{name}" слово "{word}" встречается {k} раз')



print()
print('    *****')
wfinder = Words_Finder('test_file.txt', 'test1.txt')
wfinder.get_all_words()
print()
print(' Все слова во всех файлах:')
print(wfinder.all_words)
print()
wfinder.find('нам')
print()
wfinder.count('text')
print()
print('End of lesson')
print('   --------')