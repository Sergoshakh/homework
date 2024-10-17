import fake_math as fm
import true_math as tm

print()
print('    ***')
print()
while True:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    result_fake = fm.divide(a, b)
    result_true = tm.divide(a, b)
    print(f'  fake math {a}/{b} = {result_fake}')
    print(f'  true math {a}/{b} = {result_true}')
    print()
    ans = input('Продолжить? Y/any key : ')
    
    if ans == 'y' or ans == 'Y':
        continue
    else:
        print('End of lesson')
        break
