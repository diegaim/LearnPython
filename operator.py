number = 100
if((number % 2) == 0):
    print(number, " is even number.")
else:
    print(number, " is odd number.")

#Make pyramid
loop = 10
counter = 0
while(counter < loop):
    print("*" * int(counter + 1))
    counter = counter + 1
while(counter >= 0):
    print("*" * int(counter))
    counter = counter - 1