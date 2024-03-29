def averageOfThreeNumbers(number1, number2,number3):
    return (number1+number2+number3)/3

firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number: '))
thirdNumber = int(input("Enter third number: "))
average = (averageOfThreeNumbers(firstNumber, secondNumber,thirdNumber))
print('Average of the given three numbers is', average)
