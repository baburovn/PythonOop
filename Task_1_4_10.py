import sys
class ListObject:

    def __init__(self, data):
        self.data = data
        self.next_obj = None


    def link(self, obj):
        if self.next_obj is None:
            self.next_obj  = obj
        else:
            self.next_obj.link(obj)



head_obj = ListObject(lst_in[0])
for i in lst_in[1:]:
    head_obj.link(ListObject(i))


def p(a):
    if a.next_obj is None:
        print(a.data)
        exit()
    else:
        print(a.data)
        p(a.next_obj)
p(head_obj)
