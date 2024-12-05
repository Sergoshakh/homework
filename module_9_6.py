def all_variants(text):
    for k in range(len(text)):
        txt = ''
        if k == 0:
            txt = ''
        else:
            txt = text[k-1]

        for i in range(len(text)-k):
            if k == 0:
                txt = text[i]
            else:
                txt = txt + text[i+k]
            yield txt

a1 = all_variants('abc')
print('результат работы генератора для "abc": ')
for i in a1:
    print(i)
print()
print('результат работы генератора для "abcde": ')
a2 = all_variants('abcde')
for i in a2:
    print(i)
