class DataBase:
    def __init__(self, user,psw,port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД:{self.user}, {self.psw},{self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись даты в БД {data}")
        
