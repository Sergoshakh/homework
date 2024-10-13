def calculate_structure_sum(*ds):
    global summa
    ds = list(*ds)
    for i in range(len(ds)):
        if isinstance(ds[i], str):
            obr_str(ds[i])
            continue
        if isinstance(ds[i], int):
            obr_int(ds[i])
            continue
        if isinstance(ds[i], dict):
            obr_dict(ds[i])
            continue
        calculate_structure_sum(ds[i])
    return

def obr_dict(dict_):
    global summa
    ds = list(dict_.keys()) + list(dict_.values())
    calculate_structure_sum(ds)
    return

def obr_int(number):
    global summa
    summa += number
    return

def obr_str(str_):
    global summa
    summa += len(str_)
    return summa
   
summa = 0
data_structure = [[1, 2, 3],{'a':4, 'b':5}, (6, {'cube':7, 'drum':8}),"Hello", ((),[{(2, 'Urban',('Urban2', 35))}])]
calculate_structure_sum(data_structure)

print()
print('    * * *')
print()
print(f'''Сумма всех чисел и длин строк в выражении:
{data_structure}
равна {summa}''')
print()
print('End of lesson')

