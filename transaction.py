import os


def staff():
    print(" (1)Inventory Update\n (2)Inventory Tracking\n")
    quit = False
    while not quit:
        opt = input("Please select the operation you wish to perform(Enter the option number）:")
        if opt.isdigit() and int(opt) <= 2 and int(opt) >= 1:
            if opt == "1":
                inventory_data()
            elif opt == "2":
                print("haha")
            while True:
                choice = input(
                    "Do you want to go back to the MENU or QUIT?(press 'ENTER' to 'continue' or press 'Q' to 'quit'):").upper()
                if choice == "Q":
                    quit = True
                    break
                elif choice == "":
                    quit = False
                    print("(1)Inventory Update\n (2)Inventory Tracking\n")
                    break
                else:
                    print("You must either press 'ENTER' or 'Q' to quit!")
        else:
            print("You must enter a corresponding code!")


def record_ppe_read():
    rec_ppe = []
    with open("ppe.txt", "r") as file:
        for _ in file:
            item_name, item_code, suppliers_code, stock_quantity = line.strip().split(':')
            rec_ppe.append((item_name, item_code, suppliers_code, stock_quantity))
        return rec_ppe


def inventory_data():
    rec_ppe = inventory_update()
    with open("ppe.txt", "w") as file:
        for ppe in rec_ppe:
            file.write(f"{ppe[0]},{ppe[1]},{ppe[2]},{ppe[3]}\n")


def inventory_update():
    item = input("Please Enter Code of Item: ")
    transaction = input("Please Choose Your Transaction Type(Increase/Distributed): ")
    supplier_hospital = input("Please Enter Code of Supplier or Hospital: ")
    quantity = int(input("Please Key in The Quantity of Item Increase or Distributed: "))
    date = input("Please Enter The Date of Transactions(DD/MM/YYYY): ")
    with open("transactions.txt", "a") as transaction_file:
        transaction_file.write(f"{item},{supplier_hospital},{transaction},{quantity},{date}\n")
    rec_ppe = record_ppe_read()
    for x, ppe in enumerate(rec_ppe):
        if ppe[1] == item:
            new_amount = int(ppe[3] + x)
            rec_ppe[x] = (ppe[0], ppe[1], ppe[2], str(new_amount))
            print("Congratulation, Inventory Successfully Update!")
    return rec_ppe


print('Welcome to Inventory Management System'.title())
logging_in = True
while logging_in:
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as user:
            user.write("1234,yeo,iamyeoyule,admin\n")
    with open("user.txt", "r") as user_file:
        lines = user_file.readlines()
        user_ID = input("Please enter your User ID:")
        user_name = input("Please enter your User name:").lower()
        user_password = input("Please enter your User Password:")
        i = 0
        for line in lines:
            split_line = line.split(",")
            if user_ID == split_line[0] and user_name == split_line[1] and user_password == split_line[2]:
                print("Successfully logged in")
                logging_in = False
                break
        if logging_in == True:
            print("Invalid User's Information.Please retry")
if split_line[3].strip() == "staff":
    staff()
