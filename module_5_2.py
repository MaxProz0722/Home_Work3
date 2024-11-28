
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует!')
        else:
            print(new_floor)


    def __len__(self):
        return  self.number_of_floors

    def __str__(self):
        return (f'Название:{self.name}, колличество этажей:{self.number_of_floors}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖЛ Акация', 20)
h1.go_to(5)
h2.go_to(10)
print(len(h1))
print(len(h2))
print(h1)
print(h2)
