TYPE_OS = 1 # 1 - Windows; 2 - Linux
class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    global TYPE_OS
    def __new__(cls, name, *args, **kwargs):
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
            obj.name = name
            return obj
        else:
            obj = super().__new__(DialogLinux)
            obj.name = name
            return obj
    def __init__(self,name):
        self.name = name


dg = Dialog("ne")
print(dg.name)