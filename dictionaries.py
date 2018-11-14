myDict = {}
myDict["name"] = "Diega Iqbal Mardana"
myDict["age"] = 23
print(myDict)

myDict2 = {"name" : "Diega Iqbal Mardana", "age" : 23, "ageUom" : "Years"}
print(myDict2)
myDict2.pop("ageUom")
del myDict2["age"]
print(myDict2)