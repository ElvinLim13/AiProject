def differentOfTwoNumbers(number1, number2):
    return number1-number2

firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number: '))
total = abs(differentOfTwoNumbers(firstNumber, secondNumber))
print('Different of the given two numbers is', total)