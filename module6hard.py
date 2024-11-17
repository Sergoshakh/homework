import math

class Figure:
    sides_count = 0
    def __init__(self, rgb, *sides):
        self.__sides = sides
        self.__color = rgb
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        color = [r, g, b]
        if self.__is_valid_color(color):
            self.__color = tuple(color)
            print('__цвет изенён')
        else:
            print('__некорректный цвет')
              
    def __is_valid_color(self, color):
        for i in range(3):
            if color[i] >= 0 and color[i] <= 255:
                continue
            else:
                return False
        return True
            
    def get_sides(self):
        return  list(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return #print('       len(new_sides) != sides_count')
        else:
            if self.__is_valid_sides(*new_sides) == False:
                return #print('       new_sides[n] <= 0')
            else:
                self.__sides = new_sides

    def __is_valid_sides(self, *new_sides):
        for i in range(self.sides_count):
            if new_sides[i] <= 0:
                return False
        return True

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *sides):
        self.side = 1
        if len(sides) != 1:
            self.side = 1
        else:
            self.side = sides[0]
        sides = []
        for i in range(self.sides_count):
            sides.append(self.side)

        super().__init__(rgb, *sides)

    def get_square(self):
        return math.pi * self.__radius ** 2

    def get_radius(self):
        sd = self.get_sides()
        self.__radius = sd[0] / 2 / math.pi
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, *sides):
        self.side = 1
        if len(sides) != self.sides_count:
             sides = []
             self.side = 1
             for i in range(self.sides_count):
                 sides.append(self.side)
        else:
            pass

        super().__init__(rgb, *sides)

    def get_square(self):
        sd = self.get_sides()
        p = sum(sd) / 2
        return (p * (p - sd[0])*(p - sd[1])*(p - sd[2]))**0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *sides):
        self.side = 1
        if len(sides) != 1:
            side = 1
        else:
            self.side = sides[0]
        sides = []
        for i in range(self.sides_count):
            sides.append(self.side)

        super().__init__(rgb, *sides)


    def get_square(self):
        return 6 * self.side ** 2

    def get_volume(self):
        return self.side ** 3



print()
print('    ***')
print()
print('МОИ ПРОВЕРКИ:')
print()

circle = Circle((100, 100, 100), 3, 4)

print('    class circle:')
print('sides_count =', circle.sides_count)
print('__sides ', circle.get_sides())
print('__radius =', circle.get_radius())
print('square =', circle.get_square())
print('__colors :', circle.get_color())
print('__len__ =' ,len(circle))
circle.set_color(200, 210, 220)
print('new__colors :', circle.get_color())
print('filled -', circle.filled)
circle.set_sides(30)
print('__sides ', circle.get_sides())
print('__radius =', circle.get_radius())
print('square =', circle.get_square())
print('__len__ =' ,len(circle))
print('-------------------------')
print()

triangle = Triangle((100, 100, 100), 4, 3, 9 ,4) # неправильное число сторон
print('    class triangle')
print('sides_count =', triangle.sides_count)
print('__sides ', triangle.get_sides())
triangle.set_sides(30, 40, 50) # исправляем число сторон
print('__sides ', triangle.get_sides())
print('square =', triangle.get_square())
print('__colors :', triangle.get_color())
print('filled -', triangle.filled)
print('__len__ =' ,len(triangle))
print('-------------------------')
print()

cube = Cube((100, 100, 100), 30)
print('    class cube')
print('sides_count =', cube.sides_count)
print('__sides ', cube.get_sides())
cube.set_sides(30, 40, 50)
print('__sides ', cube.get_sides())
print('square =', cube.get_square())
print('__colors :', cube.get_color())
print('filled -', cube.filled)
cube.filled = True
print('filled -', cube.filled)
print('__len__ =' ,len(cube))
print('volume ', cube.get_volume())
print('-------------------------')
print()
print('ПРОВЕРКИ ЗАДАНИЯ:')
print()
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
print()
print('End of lesson')