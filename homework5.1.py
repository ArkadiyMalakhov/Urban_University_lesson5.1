class House:
    def __init__(self, name, qty_floors):
        self.name = name
        self.qty_floors = qty_floors

    def go_to(self, new_floor):
        if self.qty_floors < 1 or self.qty_floors < new_floor:
            print('Такого этажа не существует')
        else:
            for self.qty_floors in range(1, new_floor + 1):
                print(self.qty_floors)

h1 = House('ЖК Горький', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

