from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
    
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'a')
        file.close()
        self.reeded = ''
    def get_products(self):
        file = open(self.__file_name, 'r')
        self.reeded = file.read()
        file.close()
        return self.reeded

    def add(self, *args):
        reeded = self.get_products()
        file = open(self.__file_name, 'a')
        for i in range(len(args)):
            if reeded.find(str(args[i])) == -1:
                file.write(str(args[i]))
                file.write('\n')
            else:
                print(f'Продукт {str(args[i])} уже есть в магазине')
        file.close()
        
   
    
    
s1 = Shop()

p1 = Product('Potato', 50.0, 'Vagenables')
p2 = Product('Spaghetti', 3.4, 'Grosceries')
p3 = Product('Potato', 5.5, 'Vagenables')
p4 = Product('Apple', 150.0, 'Fruits')

print('продукт1 - ',p1)
print('продукт2 - ',p2)
print('продукт3 - ',p3)
print('продукт4 - ',p4)
print()
print('До первой поставки продуктов, читаем из файла:\n', s1.get_products())
print()
s1.add(p1, p2, p3)
print()
print('После первой поставки продуктов, читаем из файла:\n', s1.get_products())
print()
s1.add(p1, p2, p3, p4)
print()
print('После второй поставки продуктов, читаем из файла:\n', s1.get_products())


