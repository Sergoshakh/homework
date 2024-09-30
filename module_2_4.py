numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
len_ = len(numbers)
primes = []
not_primes = []
is_prime = True
for i in range(1, len_):
    for j in range(1, len_):
        if numbers[i] == numbers[j]:
            continue
        else:
            if numbers[i] % numbers[j] == 0:
                is_prime = False
                not_primes.append(numbers[i])
                break
            else:
                is_prime = True
                continue
    if is_prime == True:
        primes.append(numbers[i])
print('')
print('Исходное множество: ', numbers)
print('')
print('Простые числа из этого множества: ', primes)
print('Составные числа из этого множества: ', not_primes)
print('')
print('End of lesson')
