#normal function
def SumNumber(number1, number2):
    return number1 + number2

#function with options argment
def SumNumber(number1, number2, *numbers):
    result = number1 + number2
    for cNumber in numbers:
        result = result + cNumber
    return result

#function with key oprions argument
def SumNumber(number1, number2, **options):
    action = option.get("action")
    if (action == "sum"):
        return number1 + number2
    elif (action == "div"):
        return number1 / number2
    elif (action == "substract"):
        return number1 * number2
    elif (action == "mod" | action == "modular"):
        return number1 % number2
    else:
        return number1 + number2
