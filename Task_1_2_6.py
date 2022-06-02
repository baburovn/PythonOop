import pprint
class Car:
    pass

setattr(Car, "model","Тойота")
setattr(Car, "color","Розовый")
setattr(Car, "number","О111АА77")

print(Car.__dict__["color"])
pprint.pp(Car.__dict__)