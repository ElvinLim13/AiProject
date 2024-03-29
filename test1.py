
# print('Welcome to Inventory Management System')
# user_ID=input('Please enter your user ID:')
# name=input('Please enter your name:')
# user_Type=input('Please enter your user Type(admin or staff):')
# while True:
#     if user_Type!='admin' or user_Type!='staff':
#         print('You should enter "admin" or "staff"')
#         user_Type = input('Please enter your user Type(admin or staff):')

PPEitems = {"HC": "Head Cover", "FS": "Face Shield", "MS": "Mask", "GL": "Gloves",
                "GW": "Gown", "SC": "Shoe Covers"}

# with open("transaction.txt", "w") as ppe:
#      space = "\t" * 5
#      ppe.write(f"{space}Received{space}Distributed{space}Total\n")
# with open("transaction.txt", "a") as ppe:
#      space="\t"*6
#      for i in PPEitems:
#         i=i+f":{space}{0  }{space}\t{0}{space}\t{0}\n"
#         ppe.write(i)

#记录接收ppe
def receive_ppe():
    quit = False
    while not quit:
        with open(r"C:\Users\yeo yu le\PycharmProjects\assignment\transaction.txt", "r", encoding="utf-8") as line:
            lines = line.readlines()

            variety = input("Please enter the item you want to record:").upper()
            amount = int(input("Please enter the amount of the item:"))
            variety += ":"
            for i, line in enumerate(lines):
                line = line.strip()
                line = line.split()
                if line[0] == variety:
                    pre_amount = int(line[1])
                    amountsum = 0
                    amountsum = amountsum+amount+pre_amount
                    total=int(line[3])+amountsum
                    space="\t"*6
                    modified_line=f"{line[0]}{space}{amountsum}\t{space}{line[2]}{space}{total}\n"
                    lines.pop(i)
                    lines.insert(i,modified_line)
                    choice = input(
                        'Do you want to continue recording items?(press "ENTER" if YES, press "Q" if NO):').upper()
                    if choice == "":
                        quit = False
                        with open("transaction.txt", "w") as ppe:
                            ppe.writelines(lines)
                    elif choice == "Q":
                        quit = True
                        with open("transaction.txt", "w") as ppe:
                            ppe.writelines(lines)       #       ##


#记录分发ppe
def distribute_ppe():
    quit = False
    while not quit:
        with open(r"C:\Users\yeo yu le\PycharmProjects\assignment\transaction.txt", "r", encoding="utf-8") as line:
            lines = line.readlines()

            variety = input("Please enter the item you want to record:").upper()
            amount = int(input("Please enter the amount of the item:"))
            variety += ":"
            for i, line in enumerate(lines):
                line = line.strip()
                line = line.split()
                if line[0] == variety:
                    pre_amount = int(line[2])
                    amountsum = 0
                    amountsum = amountsum + amount + pre_amount
                    total=int(line[3])-amountsum
                    space = "\t" * 6
                    modified_line = f"{line[0]}{space}{line[1]}\t{space}-{amountsum}{space}{total}\n"
                    lines.pop(i)
                    lines.insert(i, modified_line)
                    choice = input(
                        'Do you want to continue recording items?(press "ENTER" if YES, press "Q" if NO):').upper()
                    if choice == "":
                        quit = False
                        with open("transaction.txt", "w") as ppe:
                            ppe.writelines(lines)
                    elif choice == "Q":
                        quit = True
                        with open("transaction.txt", "w") as ppe:
                            ppe.writelines(lines)
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

