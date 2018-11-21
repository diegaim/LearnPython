class Person:
    _name = str()
    _age = int()

    def __init__(self):
        self._name = str()
        self._age = int()

    def SetPerson(self, name, age):
        try:
            self._name = str(name)
            self._age = int(age)
        except Exception as e:
            return str(e)

    def GetPerson(self):
        personData = {'name':self._name, 'age':self._age}
        return personData
