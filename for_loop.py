#12345
result = str()
for cNumber in range(5):
    result = result + str(cNumber+1)
print("\n" + result)

#345
result = str()
for cNumber in range(3, 6):
    result = result + str(cNumber)
print("\n" + result)

#0246810
result = str()
for cNumber in range(0, 11, 2):
    result = result + str(cNumber)
print("\n" + result)