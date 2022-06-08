class Cart:
    def __init__(self, goods=[]):
        self.goods=goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{i.name}:{i.price}" for i in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()

gd = TV("Philps",2000)
cart.add(gd)

gd = TV("Philps",5000)
cart.add(gd)

gd = Table("Lorenzo",1000)
cart.add(gd)

gd = Notebook("Lenovo", 40000)
cart.add(gd)

gd = Notebook("Asus", 50000)
cart.add(gd)

gd = Cup("CatCup", 200)
cart.add(gd)
print(cart.get_list())
cart.remove(1)
cart.remove(3)
print(cart.get_list())
