#1 defintion
def testFunction(iteration,message):
    for numebr in range(iteration):
        print("My first function! (OK thats a lie)")

print("Line Before call to function")

#suspend operation and go to the function

testFunction(5,"The message to print")

testFunction(2,"New Message")

#resume operation after call function

print("Line After call to function")
print("Lenghth of name:")