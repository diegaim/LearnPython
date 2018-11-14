class Student:
    name = str()

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

diega = Student()
diega.setName("Diega Iqbal Mardana")
print(diega.getName())