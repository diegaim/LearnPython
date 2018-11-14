myString = "Hello World!"
print("Index 'llo' is ", myString.index("llo"))
print("myString length is ", len(myString))
print(myString[0:5])
print(myString[0:5][::-1])
print(myString[myString.index("World"):myString.index("World")+len("World")])
print(myString[myString.index("World"):myString.index("World")+len("World"):2])
print(myString.upper())
print(myString.lower())