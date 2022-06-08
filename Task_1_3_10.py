lst1 = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']

FIELDS = ('id', 'name', 'old', 'salary')

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for i in data:
            self.lst_data.append({name: val for name, val in zip(FIELDS, lst1[i].split())})


    def select(self, a, b):
        return DataBase.lst_data[a:b+1]


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        passd