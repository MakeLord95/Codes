class Filefifo:
    def __init__(self, name):
        self.file = open(name)
        self.value = 0

    def put(self, value):
        pass

    def get(self):
        string = self.file.readline()
        if len(string) > 0:
            self.value = int(string)
        else:
            self.value = -1
        return self.value

    def dropped(self):
        return 0

    def empty(self):
        return False
