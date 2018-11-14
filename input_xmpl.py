from enum import Enum

class Person:
    name = str()
    objGender = str()

    def __init__(self, name, gender):
        self.name = name
        self.objGender = gender

    def GetDescription(self):
        return "Hello my name is %s. My gender is %s" % (self.name, self.objGender.value)

    def GetDescriptGender(self):
        return "Gender is from %s with selection %s and value %s" %(type(self.objGender), self.objGender.name, self.objGender.value)

    class Gender(Enum):
        MALE = "Male"
        FEMALE = "Female"

#Main
diega = Person("Diega Iqbal Mardana", Person.Gender.MALE)
print(diega.GetDescription())
print(diega.GetDescriptGender())