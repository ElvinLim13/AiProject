print('''Calculator Program
         1.ADD
         2.SUBTRACT
         3.MULTIPLY
         4.DIVIDE''')
chosen= ""

while True:
    chosen = input("Choose the operation from the given options: ")
    if chosen == "1":
        firstNumber = float(input("Enter first number: "))
        secondNumber = float(input("Enter second number: "))
        def sumOfTwoNumbers(number1, number2):
            return number1 + number2
        total = (sumOfTwoNumbers(firstNumber, secondNumber))
        print(f"Sum of {firstNumber} and {secondNumber} is {total}")
        break
    elif chosen == "2":
        firstNumber = float(input("Enter first number: "))
        secondNumber = float(input("Enter second number: "))
        def subtractOfTwoNumbers(number1, number2):
            return number1 - number2
        subtract = abs(subtractOfTwoNumbers(firstNumber, secondNumber))
        print(f"Subtract of {firstNumber} and {secondNumber} is {subtract}")
        break
    elif chosen == "3":
        firstNumber = float(input("Enter first number: "))
        secondNumber = float(input("Enter second number: "))
        def productOfTwoNumbers(number1, number2):
            return number1 * number2
        product = (productOfTwoNumbers(firstNumber,secondNumber))
        print(f"Product of {firstNumber} and {secondNumber} is {product}")
        break
    elif chosen == "4":
        firstNumber = float(input("Enter first number: "))
        secondNumber = float(input("Enter second number: "))
        def quotientOfTwoNumbers(number1, number2):
            return number1 / number2
        quotient = (quotientOfTwoNumbers(firstNumber, secondNumber))
        print(f"Quotient of {firstNumber} and {secondNumber} is {quotient}")
        break
    else:
        print('''
Syntax Error
Please choose the operation from the given option again.''')