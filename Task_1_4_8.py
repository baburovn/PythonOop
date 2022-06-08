class CPU:
    def __init__(self, name,fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name,volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name,CPU, Memory):
        self.name = name
        self.cpu = CPU
        self.total_mem_slots = 4
        if len(Memory) <= self.total_mem_slots:
            self.mem_slots = Memory

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор:{self.cpu.name},{self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"]


mb = MotherBoard("ASUS", CPU("Ryzen 4000", "2000"),[Memory("Corsair", 2),Memory("Patriot", 2)])
print(mb.get_config())