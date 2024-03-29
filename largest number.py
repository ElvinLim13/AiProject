max = None
while True :
    numbers = int(input("Enter a number :"))
    if max is None or numbers > max:
        max = numbers
    elif numbers == 0 :
        break
    else :
        print("Invalid")
if max is not None:
    print(f"The maximum value is: {max}")
else:
    print("Invalid")

