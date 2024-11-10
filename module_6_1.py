class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible:
            self.fed = True
        else:
            self.alive = False

class Mammal(Animal):
    pass

class Predator(Animal):
    ...

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    ...


class Fruit(Plant):
    edible = True

a1 = Predator('Волк Ди Каприо')
a2 = Mammal('Хатико')
p1 = Flower('цветик-семицветик')
p2 = Fruit('Заводной апельсин')

print()
print('    *****')
print()

a1.eat(p1)
print(f'{a1.name} не стал есть {p1.name} и теперь его статус: живой = {a1.alive}, сытый = {a1.fed}')
a2.eat(p2)
print(f'{a2.name} съел {p2.name} и теперь его статус: живой = {a2.alive}, сытый = {a2.fed}')

print()
print('End of lesson')
print('   --------')


