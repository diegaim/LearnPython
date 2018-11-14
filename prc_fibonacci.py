def GetFibonacci(number):
    if(number == 1):
        return number
    return number * GetFibonacci(number - 1)

fib = GetFibonacci(5)
print(str(fib))