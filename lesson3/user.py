class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirst(self):
        print(self.first_name)

    def sayLast(self):
        print(self.last_name)

    def sayFull(self):
        print(self.first_name, self.last_name)