def is_prime(func):
    def wripper(*args):
        n = func(*args)
        for k in range(2, n):
            if n % k == 0 and n != k :
                prst = False
                break
            else:
                prst = True
        if prst:
            print(f'{n} - число простое')
        else:
            print(f'{n} - число составное')
        return n
    return wripper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


print()
result = sum_three(2, 3, 6)
print('sum_three = ', result)
print()
result = sum_three(2, 4, 6)
print('sum_three = ', result)

