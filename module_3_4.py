def single_root_words(root_word, *other_words):
    tmp_root = root_word.lower() # определяем временное значение root_word
    tmp_ow = list(other_words)   # определяем временные значения other_words
    same_words = []
    for i in range(len(other_words)):
        tmp_ow[i] = other_words[i].lower()
        if tmp_root in tmp_ow[i] or tmp_ow[i] in tmp_root:
            same_words.append(other_words[i])
    return same_words, root_word, other_words # возвращаем результат работы функции и оригиналы root_word и other_words

result1 = single_root_words('Rich', 'richiest', 'Orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print('')
print('    * * *')
print('')
print(f"""Корень '{result1[1]}' из списка {result1[2]}
имеют слова: {result1[0]}""")
print('')
print(f"""Однокоренные слову '{result2[1]}' из списка {result2[2]}
являются слова: {result2[0]}""")
print('')
print('End of lesson')
