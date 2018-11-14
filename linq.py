from generators import GetSixRandomNumber

def PrintListNumber(listNumber):
    counter = int(1)
    for cNumber in listNumber:
        print("Data number %d = %d" %(counter, cNumber))


#Main Program
randomNumber = GetSixRandomNumber()
positiveNumber = [int(x) for x in randomNumber if x > 0]
PrintListNumber(positiveNumber)