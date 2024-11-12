import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,speed):
        self._cords = [0 ,0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        z = self._cords[2] + dz * self.speed
        if z < 0:
            print('It is too deep, i can not dive!')
        else:
            self._cords[2] += dz * self.speed


    def get_cords(self):
        x,y,z = self._cords
        print(f'X: {x}, Y: {y}, Z: {z}')
        #print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Sorry, i am peaceful')
        else:
            print('Be careful, i am attacking you!!!')


class Bird(Animal):
    beak = True
    def lay_eggs(self):
        num_eggs = random.randint(1,4)
        print(f'Here is(are) {num_eggs} agg(aggs) for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.speed = self.speed / 2
        self._cords[2] -= abs(dz) * self.speed

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class DuckBill(Bird, AquaticAnimal, PoisonousAnimal):
    _DEGREE_OF_DANGER = PoisonousAnimal._DEGREE_OF_DANGER
    sound = "Click-click-click"
    def speak(self):
        print(self.sound)

print()
print('    *****')
print()
print('bd')
brd = Bird(20)
brd.get_cords()
brd.move(2,2,-2)
brd.get_cords()
brd.attack()

print()

db = DuckBill(10)
print('live ', db.live)
print('beak ', db.beak)
db.speak()
db.attack()
db.get_cords()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
print()
print('End of lesson')
print('   --------')
