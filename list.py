myList = []
myList.append("Diega")
myList.append("Iqbal")
myList.append("Mardana")
myList.append(23)

fullName = str()
age = str()
for name in myList:
    if(type(name) == type(int())):
        age = str(name) + " years old."
    else:
        fullName = fullName + str(name) + " "
print(fullName, age)