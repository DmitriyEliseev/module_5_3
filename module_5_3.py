class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor} - Такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return h1.number_of_floors == h2.number_of_floors

    def __lt__(self, other):
        return h1.number_of_floors < h2.number_of_floors

    def __le__(self, other):
        return  h1.number_of_floors <= h2.number_of_floors

    def __gt__(self, other):
        return h1.number_of_floors > h2.number_of_floors

    def __ge__(self, other):
        return h1.number_of_floors >= h2.number_of_floors

    def __ne__(self, other):
        return h1.number_of_floors != h2.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
        return self



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)