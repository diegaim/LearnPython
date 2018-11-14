import random

def GetSixRandomNumber():
    for cNumber in range(6):
        yield random.randint(0, 256)

sixRandomNumber = GetSixRandomNumber()
print("Type of sixRandomNumber variable is %s" % str(type(sixRandomNumber)))

#Print generator values
for cRandomNbr in sixRandomNumber:
    print("Data : %d" %cRandomNbr)