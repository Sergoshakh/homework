def apply_all_func(int_list, *functions):
    results = {}
    for f in functions:
        results[f.__name__] = f(int_list)
    return results

int_list = [6, 20, 15, 9]
print(apply_all_func(int_list, max, min))
print(apply_all_func(int_list,len, sum, sorted))