import sys

class StreamData:
    '''который бы на входе получал список полей FIELDS (передается в атрибут fields) и список строк lst_in
    (передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с
    именами полей из fields и соответствующими значениями из lst_values.'''

    def create(self, fields, lst_values):
        self.fields = fields
        self.lst_in = lst_values
        if self.fields != None and self.lst_in != None:
            return True

        elif len(self.fields) != len(self.lst_in):
            return False
        else: return False

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res