class Translator:
    my_dict = dict()

    def add(self, eng, rus):
        ''' добавляем множественное значение к ключу '''
        if eng not in self.my_dict:
            self.my_dict[eng] = list()
        self.my_dict[eng].append(rus)
        return self.my_dict

    def remove(self, eng):
        if eng in self.my_dict:
            self.my_dict.pop(eng)

    def translate(self, eng):
        if eng in self.my_dict:
            return self.my_dict[eng]

tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate("go"))