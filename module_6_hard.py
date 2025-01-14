import  math

class Figure:
    sides_count = 0
    filled = bool

    def __init__(self, *__color, **__sides):
        __sides = []
        __color = []

    def get_color(self, r, g, b):
        print(self.__color)

    def __is_valid_color(self, r, g, b):
        for i in self.__color:
            if i > 0:
                True
            if i < 256:
                True
            else:
                False

    def set_color(self, r, g, b):
        if self.__is_valid_color() == True:
            self.__color = []
        else:
            self.__color = self.__color

    def __is_valid_sides(self, *args):
        if self.args > 0 and self.args == len(self.__sides):
            True
        else:
            False

    def get_sides(self):
        print(self.__sides)

    def __Len__(self):
        self.__radius = self.__sides[0] / 2 * math.pi
        с = 2 * math.pi * self.__radius
        print(с)

    def set_sides(self, *new_sides):
        if self.new_sides == self.sides_count:
            self.sides_count = self.new_sides
        if self.new_sides != self.sides_count:
            self.sides_count = self.sides_count

class Circle(Figure):
    sides_count = 1

    def __init__(self, __colors, __sides):
        super().__init__(self, __colors)
        self.__radius = self.__sides[0] / 2 * math.pi


    def get_square(self):
        circle_s = math.pi * self.__radius**2
        print(circle_s)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __sides):
        super().__init__(self, __sides)

    def get_square(self, __sides):
        a = __sides[0]
        b = __sides[1]
        c = __sides[2]
        p = (a + b + c) / 2
        s = float('%.6f' % math.sqrt(p * (p - a) * (p - b) * (p - c)))
        print(s)

class Cube(Figure):

    def __init__(self, __colors, __sides):
        super().__init__(self, __colors, __sides)
        sides_count = 12
        while len(self.__sides) <= sides_count:
            __sides.append(__sides)
            break

    def get_volume(self, __sides):
        s = __sides**3
        print(s)


    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
