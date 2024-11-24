def add_everything_up(a, b):
    try:
        print(f' - складываем {type(a)} {a} и {type(b)} {b}')
        c = a + b
    except TypeError as exc:
        print(f'выскакивает исключение: {exc}')
        a = str(a)
        b = str(b)
        c = a + b
        print('   однако путём обработки этого исключения получаем результат:')
        return c
    else:
        return c
    finally:
        print('результат такого сложения:') 

print(add_everything_up(25, 45))
print()
print(add_everything_up('25', 45))
print()
print(add_everything_up(25.5, 'apple'))
print()
print(add_everything_up('banana', 'apple'))

