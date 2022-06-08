class TriangeChecker:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        type_ch = (self.a,self.b,self.c)
        for i in type_ch:
            if not isinstance(i, int):
                return 1
            if i <= 0:
                return 1


        if  ((self.a + self.b) <= self.c or (self.b + self.c) <= self.a or (self.a + self.c) <= self.b):
            return 2
        if ((self.a + self.b) > self.c or (self.b + self.c) > self.a or (self.a + self.c) > self.b):
            return 3

tr = TriangeChecker(3,4,2)
print(tr.is_triangle())
