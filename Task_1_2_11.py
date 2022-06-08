class Person:
    name = "Сергей Балакирев"
    job = 'Программист'
    city = 'Москва'

p1 = Person()
# print(hasattr(p1, "job")) - нужно локальное свойство)
print(getattr(Person, "jj"))
