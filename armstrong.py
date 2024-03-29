number = (input("Enetr number to check if it's armstrong: "))
length = len(number)
number = int(number)

original = number
armstrong = 0

while number > 0:
    remainder = number % 10
    armstrong = armstrong + remainder**length
    number = number // 10

if original == armstrong :
    print(original," is An ArmStrong.")

else:
    print(original, " is not an Armstrong.")