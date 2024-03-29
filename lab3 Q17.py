max = None

while True :
        number=int(input("Enter a number: "))
        if number == 0 :
            break
        elif max is None or number > max :
            max = number
        else :
            print("Invalid")
if max is not None:
    print(f"The maximum value is : {max}")
else :
    print("Not Valid")
