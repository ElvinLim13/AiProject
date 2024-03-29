import os
from typing import TextIO, List


# admin的功能选择
def admin():
    print(
        ' (1)add new user\n (2)modify user\n (3)search user\n (4)delete users\n (5)record PPE items\n (6)record Suppliers details')
    quit = False
    while not quit:
        opt = input("Please select the operation you wish to perform(Enter the option number）:")
        if opt.isdigit() and int(opt) <= 6 and int(opt) >= 1:
            if opt == "1":
                add_newuser()
            elif opt == "2":
                modify_user()
            elif opt == "3":
                search_user()
            elif opt == "4":
                delete_user()
            elif opt == "5":
                if not os.path.exists("suppliers.txt"):
                    print("Please create a Supplier File first!")
                else:
                    record_ppe()
            elif opt == "6":
                record_suppliers()
            while True:
                choice = input(
                    "Do you want to go back to the MENU or QUIT?(press 'ENTER' to 'continue' or press 'Q' to 'quit'):").upper()
                if choice == "Q":
                    quit = True
                    break
                elif choice == "":
                    quit = False
                    print(
                        ' (1)add new user\n (2)modify user\n (3)search user\n (4)delete users\n (5)record PPE items\n (6)record Suppliers details')
                    break
                else:
                    print("You must either press 'ENTER' or 'Q' to quit!")
        else:
            print("You must enter a corresponding code!")


# 添加新用户

def add_newuser():
    with open("user.txt", "a") as user:
        while True:
            id = input("Please enter NEW User's ID:")
            with open("user.txt", "r") as user:
                lines = user.readlines()
            found = False
            for line in lines:
                if id == line.split(",")[0]:
                    found = True
                    print("This ID has been used.Please take another ID")
            if not found:
                if id.isdigit() and len(id) == 4:
                    break
                else:
                    print("User ID should be 4 digit numbers")

        name = input("Please enter NEW User's name:").lower()

        while True:
            password = input("Please enter NEW User's password:")
            if len(password) < 8 or len(password) > 16:
                print("User's password should be 8-16 characters!")
            else:
                break

        while True:
            usertype = input("Please enter NEW User's Type:")
            if usertype == "admin" or usertype == "staff":
                break
            else:
                print("The User Type should be 'staff' or 'admin' only!")
        tup1 = (id, name, password, usertype)
        user_list = list(tup1)
        user.writelines(f"{','.join(user_list)}\n")


# 更改用户资料
def modify_user():
    with open("user.txt", "r") as user:
        lines = user.readlines()

    while True:
        opt = input("Please enter the user's ID you want to modify : ")

        found = False

        for i, line in enumerate(lines):
            for j in line.split(","):
                if opt == j:
                    found = True
                    break
                break

        if found:
            while True:
                new_id = input("Please enter CORRECT user's ID:")
                if new_id.isdigit() and len(new_id) == 4:
                    break
                else:
                    print("User ID should be 4 digit numbers")

            new_name = input("Please enter CORRECT user's name:").lower()

            while True:
                new_password = input("Please enter CORRECT user's password:")
                if len(new_password) < 8 or len(new_password) > 16:
                    print("User's password should be 8-16 characters!")
                else:
                    break

            while True:
                new_usertype = input("Please enter CORRECT user's Type:")
                if new_usertype == "admin" or new_usertype == "staff":
                    break
                else:
                    print("The User Type should be 'staff' or 'admin' only!")
            line = f"{new_id},{new_name},{new_password},{new_usertype}\n"
            lines[i] = line

            with open("user.txt", "w") as user:
                user.writelines(lines)
                print("The User's information has been successfully modified")
            break
        else:
            print(f"User with ID '{opt}' not found in the file.")


# 删除用户资料
def delete_user():
    while True:
        with open("user.txt", "r") as user:
            lines = user.readlines()

        opt = input("Please enter the User's ID you want to delete : ")

        found = False

        for i, line in enumerate(lines):
            for j in line.split(","):
                if opt == j:
                    found = True
                    break

        if found:
            del lines[i]
            with open("user.txt", "w") as user:
                user.writelines(lines)
                print("The User's information has been successfully deleted")
            break

        else:
            print(f"User with ID '{opt}' not found in the file.")


# 搜索用户资料
def search_user():
    with open("user.txt", "r") as user:
        lines = user.readlines()

    opt = input("Please enter the User's ID you want to search : ")

    found = False

    for line in lines:
        split_line = line.split(",")
        for i, j in enumerate(split_line):
            if opt == j:
                print(
                    f"User ID:{split_line[i]}\nUser Name:{split_line[i + 1]}\nUser Password:{split_line[i + 2]}\nUser Type:{split_line[i + 3]}")
            found = True
            break
    if not found:
        print('The User does not exist')


# 我拿来创建ppe.txt的函式
def record_ppe():
    ItemCode = ['HC', 'FS', 'MS', 'GL', 'GW', 'SC']
    Item_Name = ['Head Cover', 'Face Shield', 'Mask', 'Gloves', 'Gown', 'Shoe Covers']
    Item_Details = zip(ItemCode, Item_Name)
    suppliers = {}
    if os.path.exists("suppliers.txt"):
        with open("suppliers.txt", "r") as supplier:
            lines = supplier.readlines()

            for line in lines:
                line = line.split(":")
                suppliers[line[0]] = line[1].strip()
            print(suppliers)
    print("\nPPE ITEMS RECORD SYSTEM")
    print(" (1)create PPE file\n (2)update PPE file\n (3)print PPE details")
    while True:
        choice = input("Please enter your option number:")
        if choice == "1":
            if not os.path.exists("ppe.txt"):
                with open("ppe.txt", "w") as ppe:
                    for k, j in Item_Details:
                        while True:
                            opt = input(f"Please enter the supplier code for {k}:").upper()
                            if opt not in list(suppliers.values()):
                                print("The supplier doesn't exist!\n")
                            else:
                                ppe.write(f"{j},{k},{opt},{100}\n")
                                break
                    break
            else:
                with open("ppe.txt", "w") as ppe:
                    for k, j in Item_Details:
                        while True:
                            opt = input(f"Please enter the supplier code for {k}:").upper()
                            if opt not in list(suppliers.values()):
                                print("The supplier doesn't exist!\n")
                            else:
                                ppe.write(f"{j},{k},{opt},{100}\n")
                                break
                    break
        elif choice == "2":
            if not os.path.exists("ppe.txt"):
                print("You cannot update PPE data without PPE file!Please create a file first.")
            else:
                dic = dict(Item_Details)
                with open("ppe.txt", "r") as ppe:
                    lines = ppe.readlines()

                    found = False

                    while True:
                        item = input("Please enter the Item Code you want to record:").upper()
                        if item not in ItemCode:
                            print("This item doesn't exist.Please try again")
                        else:
                            opt = input(f"Please enter the supplier code for {item}:").upper()
                            if opt not in list(suppliers.values()):
                                print("The supplier doesn't exist!")
                            else:
                                break
                    for i, line in enumerate(lines):
                        for n in line.split(","):
                            if item == n:
                                found = True
                                break
                        if found:
                            lines[i] = f"{dic[item]},{item},{opt},{100}\n"
                            break

                    with open("ppe.txt", "w") as ppe:
                        ppe.writelines(lines)
                    while True:
                        decision = input(
                            "Do you want to continue updating PPE data?(enter 'Yes' to continue OR 'No' to quit):").capitalize()
                        if decision == "No":
                            quit = True
                            break
                        elif decision == "Yes":
                            quit = False
                            break
                        else:
                            print("Your input should be 'Yes' or 'No' only!")
                break
        elif choice == "3":
            if not os.path.exists("ppe.txt"):
                print("You cannot print PPE details without PPE file!Please create a file first.")
            else:
                with open("ppe.txt", "r") as ppe:
                    lines = ppe.readlines()

                    space = "\t" * 3
                    horizontal_line = "---" * 30
                    print(f"{horizontal_line}\n"
                          f"Item Name{space}Item Code{space}Supplier Code{space}Quantity In stock(boxes)\n"
                          f"{horizontal_line}\n")
                    for line in lines:
                        line = line.split(",")
                        print(f"{line[0]:<13}{space}{line[1]:<10}{space}{line[2]:<10}{space}{line[3]:>10}")
                    break
        else:
            print("Invalid option!Please try again.")
    print("Command executed successfully")


# 记录supplier信息的函式
def record_suppliers():
    # "YuLe SDN.BHD": "YL", "Sam Enterprise": "SA", "Jun Siong Trading": "JS"
    suppliers = {}
    print("\nSuppliers' Detail Record System")
    while True:
        print(" (1)Record Suppliers' Details\n (2)Print Suppliers' Details")
        choice = input("Please enter your option number:")
        if choice == "1":
            if os.path.exists("suppliers.txt"):
                with open("suppliers.txt", "w") as supplier:
                    for _ in range(3):
                        supplier_name = input("Please enter the supplier's name:")
                        supplier_code = input("Please give this supplier a supplier code:").upper()
                        suppliers[supplier_name] = supplier_code
                    for key, value in suppliers.items():
                        supplier.write(f"{key}:{value}\n")
                print("Suppliers File has been created successfully!")
                break
            else:
                with open("suppliers.txt", "w") as supplier:
                    for _ in range(3):
                        supplier_name = input("Please enter the supplier's name:")
                        supplier_code = input("Please give this supplier a supplier code:").upper()
                        suppliers[supplier_name] = supplier_code
                    for key, value in suppliers.items():
                        supplier.write(f"{key}:{value}\n")
                print("Suppliers File has been created successfully!")
                break
        elif choice == "2":
            if not os.path.exists("suppliers.txt"):
                print("You must create a Suppliers first!")
            else:
                print("-----------------------------------------------\n"
                      "Suppliers' Name\t\t\t\tSuppliers Code\n"
                      "-----------------------------------------------\n")
                with open("suppliers.txt") as supplier:
                    lines = supplier.readlines()

                for line in lines:
                    line = line.split(":")
                    print(f"{line[0]:<35}{line[1]}")
                break
        else:
            print("Invalid option.Please try again")


def ppe_read():
    rec_ppe = []
    with open("ppe.txt", "r") as file:
        for _ in file:
            item_name, item_code, suppliers_code, stock_quantity = line.strip().split(',')
            rec_ppe.append((item_name, item_code, suppliers_code, stock_quantity))
        return rec_ppe


def inventory_update():
    item_code = input("Please Enter Code of Item: ")
    transaction = input("Please Choose Your Transaction Type(Increase/Distributed): ")
    supplier_hospital = input("Please Enter Code of Supplier or Hospital: ")
    quantity = int(input("Please Key in The Quantity of Item Increase or Distributed: "))
    date = input("Please Enter The Date of Transactions(DD/MM/YYYY): ")
    with open("transactions.txt", "a") as transaction_file:
        transaction_file.write(f"{item_code},{supplier_hospital},{transaction},{quantity},{date}\n")
    rec_ppe = ppe_read()
    for x, ppe in enumerate(rec_ppe):
        if ppe[1] == item_code:
            new_amount = int(ppe[3] + x)
            rec_ppe[x] = (ppe[0], ppe[1], ppe[2], str(new_amount))
            print("Congratulation, Inventory Successfully Update!")
    return rec_ppe


def write_new_inventory_data():
    rec_ppe = inventory_update()
    with open("ppe.txt", "w") as file:
        for ppe in rec_ppe:
            file.write(f"{ppe[0]},{ppe[1]},{ppe[2]},{ppe[3]}\n")


def staff():
    print(" (1)Inventory Update\n (2)Inventory Tracking\n")
    quit = False
    while not quit:
        opt = input("Please select the operation you wish to perform(Enter the option number）:")
        if opt.isdigit() and int(opt) <= 2 and int(opt) >= 1:
            if opt == "1":
                write_new_inventory_data()
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
            split_line: list[str] = line.split(",")
            if user_ID == split_line[0] and user_name == split_line[1] and user_password == split_line[2]:
                print("Successfully logged in")
                logging_in = False
                break
        if logging_in == True:
            print("Invalid User's Information.Please retry")
if split_line[3].strip() == "admin":
    admin()
if split_line[3].strip() == "staff":
    staff()
