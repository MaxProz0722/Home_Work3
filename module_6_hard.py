class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = bool

    def __init__(self):
        pass

    def get_color(self):
        print(self.__color)

    def __is_valid_color(self):
        for i in self.__color:
            if i > 0:
                True
            if i < 256:
                True
            else:
                False

    def set_color(self, r, g, b):
        if self.__is_valid_color() == True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if self.*args > 0 and self.*args == len(self.__sides):
            True
        else:
            False

    def get_sides(self):
        print(self.__sides)

    def __Len__(self):
        pass

    def set_sides(self, *new_sides):
        if self.*new_sides == self.sides_count:
            self.sides_count = self.*new_sides
        if self.*new_sides != self.sides_count:
            self.sides_count = self.sides_count

class Circle(Figure):
    sides_count = 1

    def __init__(self):
        super.__init__()

class Triangle:
class Cube:


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
