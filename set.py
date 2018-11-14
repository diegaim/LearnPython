#Extract word in sentence
lineWords = "my name is Eric and Eric is my name"
wordInLine = set(lineWords.split(" "))
print(wordInLine)

#Get intersection between 2 list
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.intersection(b))
print(b.intersection(a))

#Get name who not attend at only one event
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

#Get name who not attend at one party at not the other
print(a.difference(b))
print(b.difference(a))

#Get all invitation
print(a.union(b))
print(b.union(a))