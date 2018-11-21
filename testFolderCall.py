from TestFolder import *

person1 = Person.Person()
person1.SetPerson("Diega Iqbal Mardana", 23)
person1Data = person1.GetPerson()
print("The person have name %s and age %d." % (person1Data["name"], person1Data["age"]))