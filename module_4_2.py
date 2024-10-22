def test_function():
    print('работает test_fonction')
    def  inner_function():
        print('  работает inner_fonction:')
        print('  Я в области видимости функции test_function')
        return
    inner_function()
    return

test_function()
#inner_function()  => запуск невозможен, поскольку функция inner_function() не видна в глобальбном пространстве имён.
