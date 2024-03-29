number = int(input("Enter a number to make timetable "))
count = 0
while count < 10 :
    count = count+1
    ans = int(count * number)
    print(f"{number} * {count} = {ans}")