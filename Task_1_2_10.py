class Figure:
    type = "ellipse"
    color =  "red"

    def __init__(self, start_pt, end_pt, color):
        self.start_pt = start_pt
        self.end_pt = end_pt
        self.color = color




fig1 = Figure(start_pt=(10,5), end_pt=(100, 20), color="blue")
#fig1.__delattr__('color')
del fig1.color
print(*fig1.__dict__)