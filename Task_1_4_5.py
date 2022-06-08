import random as rd
class Line:
    def __init__(self,a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a,b)
        self.ep = (c,d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a,b)
        self.ep = (c,d)

def rand_n():
    return rd.randint(-100,100)


class_lst = [Line,Rect,Ellipse]
elements = [rd.choice(class_lst)(rand_n(),rand_n(),rand_n(),rand_n()) for i in range(1,218)]

for i in elements:
    if type(i) == Line:
        setattr(i, "sp", (0, 0))
        setattr(i, "ep", (0, 0))