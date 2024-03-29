#Yeo Yu Le, Lim Jun Siong
#TP074888, TP074165

import os
from datetime import datetime
import time

#admin interface
def admin():
    quit=False
    while not quit:
        print("===================================")
        print("         Admin Interface")
        print("===================================")
        print(' (1) Admin Functionalities System\n (2) File Management (PPE, Suppliers, Hospital)\n'
              ' (3) Transaction Functionalities Menu\n (4) Inventory Tracking Functionalities Menu\n'
              ' (5) Search Functionalities Menu\n (6) Log Out')
        print("===================================")
        opt=input("Please select the operation you wish to perform(Enter the option number）:")
        if opt.isdigit() and int(opt)<=6 and int(opt)>=1:
            if opt=="1":
                admin_menu()
            elif opt == "2":
                result1=file_management()
            elif opt == "3":
                result2=transaction_menu()
            elif opt == "4":
                result3=tracking_menu()
            elif opt=="5":
                result4=search_functionalities_menu()
            else:
                print("--------Thank You for using Inventory Management System--------")
                exit()
        else:
            print("You must enter a corresponding code!")
    return result1,result2,result3,result4


#for admin to choose add,modify,delete or search user
def admin_menu():
    quit = False
    while not quit:
        print("===================================")
        print("   Admin Functionalities Menu")
        print("===================================")
        print(' (1)Add New User\n (2)Modify User\n (3)Search User\n (4)Delete Users\n (5)Back')
        print("===================================")

        opt = input("Please enter your option number:")
        if opt.isdigit() and int(opt) <= 5 and int(opt) >= 1:
            if opt == "1":
                add_newuser()
            elif opt == "2":
                modify_user()
            elif opt == "3":
                search_user()
            elif opt == "4":
                delete_user()
            else:
                admin()
        else:
            print("You must enter a corresponding code!")

#add new user data
def add_newuser():
    with open("user.txt", "r") as user_read:
        lines = user_read.readlines()

    while True:
        id = input("Please enter NEW User's ID:")
        found = False
        for line in lines:
            if id == line.split(",")[0]:
                found = True
                print("This ID has been used. Please choose another ID.")
                break

        if not found:
            if id.isdigit() and len(id) == 4:
                break
            else:
                print("User ID should be 4-digit numbers")

    while True:
        name = input("Please enter NEW User's name:").strip().lower()
        if not name:
            print("Your name cannot be empty")
        else:
            break

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
    print('The user has been successfully added!')

    with open("user.txt", "a") as user:
        user.writelines(f"{','.join(user_list)}\n")

#modify user data
def modify_user():
    with open("user.txt", "r") as user:
        lines = user.readlines()

    optioning=True
    while optioning:
        opt = input("Please enter the user's ID you want to modify : ")

        found = False

        for i, line in enumerate(lines):
            if opt==line.split(",")[0]:
                found = True

                while True:
                    new_id = input("Please enter MODIFIED user's ID:")
                    find = False
                    for line in lines:
                        if new_id == line.split(",")[0]:
                            find = True
                            print("This ID has been used. Please choose another ID.")
                            break
                    if not find:
                        if new_id.isdigit() and len(new_id) == 4:
                            break
                        else:
                            print("User ID should be 4 digit numbers")

                while True:
                    new_name = input("Please enter MODIFIED User's name:").strip().lower()
                    if not new_name:
                        print("Your name cannot be empty")
                    else:
                        break

                while True:
                    new_password=input("Please enter MODIFIED user's password:")
                    if len(new_password) < 8 or len(new_password) > 16:
                        print("User's password should be 8-16 characters!")
                    else:
                        break

                while True:
                    new_usertype = input("Please enter MODIFIED user's Type:")
                    if new_usertype == "admin" or new_usertype == "staff":
                        break
                    else:
                        print("The User Type should be 'staff' or 'admin' only!")
                line=f"{new_id},{new_name},{new_password},{new_usertype}\n"
                lines[i] = line

                with open("user.txt", "w") as user:
                    user.writelines(lines)
                    print("The User's information has been successfully modified")
                break
            optioning=False
        if not found:
            print(f"User with ID '{opt}' not found in the file.")

#delete user data
def delete_user():
    while True:
        with open("user.txt", "r") as user:
            lines = user.readlines()

        opt = input("Please enter the User's ID you want to delete : ")

        found = False

        for i, line in enumerate(lines):
            for j in line.split(","):
                if opt==j:
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

#search user data and print it out
def search_user():
    with open("user.txt", "r") as user:
        lines = user.readlines()

    opt = input("Please enter the User's ID you want to search : ")

    found = False

    for line in lines:
        split_line=line.split(",")
        if opt==split_line[0]:
            print(f"User ID:{split_line[0]}\nUser Name:{split_line[1]}\nUser Password:{split_line[2]}\nUser Type:{split_line[3]}")
            found = True
            break
    if not found:
        print('The User does not exist.Please try again\n')

#staff interface
def staff():
    print("===================================")
    print("         Staff Interface")
    print("===================================")
    print(" (1) File Management (PPE, Suppliers, Hospital)\n (2) Transaction Functionalities Menu\n "
          "(3) Inventory Tracking Functionalities Menu\n (4) Search Functionalities Menu\n (5) Log Out")
    print("===================================")
    quit = False
    while not quit:
        opt = input("Please select the operation you wish to perform(Enter the option number）:")
        if opt.isdigit() and int(opt) <= 5 and int(opt) >= 1:
            if opt == "1":
                result1=file_management()
            elif opt == "2":
                result2=transaction_menu()
            elif opt=="3":
                result3=tracking_menu()
            elif opt=="4":
                result4=search_functionalities_menu()
            else:
                print("--------Thank You for using Inventory Management System--------")
                exit()
        else:
            print("You must enter a corresponding code!")
    return result1,result2,result3,result4


def transaction_menu():
    if not os.path.exists("ppe.txt"):
        print("Please create a PPE file first to record the information of the transaction")
    else:
        while True:
            print("===================================")
            print(" Transaction Functionalities Menu")
            print("===================================")
            print(" (1) Received Item from the Supplier\n (2) Distributed Item to Hospital\n (3) Back")
            print("===================================")
            choice=int(input("Please enter your choice('1' or '2' or '3'):"))
            while choice<1 or choice>3:
                print("You can only input '1' or '2' or '3'.Please try again")
                choice=int(input("Please enter your choice('1' or '2' or '3'):"))
            if choice==1:
                receive_ppe()
            elif choice==2:
                distribute_ppe()
            else:
                break
        return "back"


#record the transaction of receiving PPE
def received_item():
    from datetime import datetime

    while True:
        item_code = input("Please Enter the Code of the Item: ").upper()
        with open("ppe.txt", "r") as ppe:
            lines = ppe.readlines()
        found = False
        for line in lines:
            if line.split(",")[1] == item_code:
                found = True
        if not found:
            print("The Item Code you entered doesn't exist. Please try again.")
        else:
            break

    while True:
        try:
            quantity = int(input("Please Key in The Quantity of the Item: "))
            break
        except ValueError as error:
            print("You can only enter digit numbers only! Please try again.")

    while True:
        print("Please Enter The Date of this Transaction (Day, Month, Year)")
        try:
            day = int(input("a. Day: "))
            month = int(input("b. Month: "))
            year = int(input("c. Year: "))
            date_obj = datetime(year, month, day).date()
            formatted_date = date_obj.strftime("%d/%m/%Y")
            break
        except ValueError as e:
            print("Invalid date input:")
            print("Please enter a valid date.\n")

    with open("ppe.txt", "r") as ppe:
        lines = ppe.readlines()
        for line in lines:
            line = line.split(",")
            if line[1] == item_code:
                supplier = line[2]

    with open("transaction.txt", "a+") as transaction:
        transaction.write(f"{formatted_date},Received,{item_code},{supplier},{quantity}\n")
        print("------Transaction recorded successfully------")
    return item_code, quantity


#record transaction of distributing PPE
def distribute_item():
    from datetime import datetime

    while True:
        item_code = input("Please Enter the Code of the Item: ").upper()
        with open("ppe.txt","r") as ppe:
            lines=ppe.readlines()
        found=False
        for line in lines:
            if line.split(",")[1]==item_code:
                found=True
        if not found:
            print("The Item Code you entered doesn't exist.Please try again.")
        else:
            break

    while True:
        try:
            quantity = int(input("Please Key in The Quantity of the Item Distributed:"))
            break
        except ValueError as error:
            print("You can only enter digit number only!Please try again.")

    while True:
        hospital=input("Please enter the hospital code:").upper()
        with open("hospital.txt") as h:
            lines=h.readlines()
        found=False
        for line in lines:
            if line.split(",")[1].strip()==hospital:
                found=True
        if not found:
            print("The Hospital Code you entered doesn't exist.Please try again.")
        else:
            break

    while True:
        print("Please Enter The Date of this Transaction (Day, Month, Year)")
        try:
            day = int(input("a. Day: "))
            month = int(input("b. Month: "))
            year = int(input("c. Year: "))
            date_obj = datetime(year, month, day).date()
            formatted_date = date_obj.strftime("%d/%m/%Y")
            break
        except ValueError as e:
            print("Invalid date input:", e)
            print("Please enter a valid date.\n")

    return item_code,quantity,formatted_date,hospital

#record transaction data in "transaction.txt" and "ppe.txt"
def receive_ppe():
    rec_ppe = received_item()
    item_code,quantity=rec_ppe
    with open("ppe.txt", "r") as file:
        lines=file.readlines()

        for i,line in enumerate(lines):
            modified_line=line.strip().split(",")
            if modified_line[1]==item_code:
                ppe_amount=int(modified_line[3])
                ppe_amount+=quantity
                modified_line[3]=str(ppe_amount)
                line=",".join(modified_line)+"\n"
                lines[i]=line

        with open("ppe.txt","w") as ppe:
            ppe.writelines(lines)

#record transaction data in "transaction.txt", "distribution.txt" and "ppe.txt"
def distribute_ppe():
    enter=True
    while enter:
        rec_ppe = distribute_item()
        item_code,quantity,formatted_date,hospital=rec_ppe
        with open("ppe.txt", "r") as file:
            lines=file.readlines()

            for i,line in enumerate(lines):
                modified_line=line.strip().split(",")
                if modified_line[1]==item_code:
                    if int(modified_line[3]) - quantity <= 0:
                        print(f"The stock for {item_code} is insufficient to distribute.Please try again\n"
                              f"{item_code}'s Current Stock Available--->{modified_line[3]}")
                    else:
                        ppe_amount=int(modified_line[3])
                        ppe_amount-=quantity
                        modified_line[3]=str(ppe_amount)
                        line=",".join(modified_line)+"\n"
                        lines[i]=line
                        with open("transaction.txt", "a+") as transaction:
                            transaction.write(f"{formatted_date},Distributed,{item_code},{hospital},-{quantity}\n")

                        with open("distribution", "a+") as distribution:
                            distribution.write(f"{formatted_date},{item_code},{hospital},-{quantity}\n")

                        print("------Distribution recorded successfully------")
                        enter=False

        with open("ppe.txt","w") as ppe:
            ppe.writelines(lines)



#menu for item inventory tracking
def tracking_menu():
    status = False
    while status == False:
        print("===================================")
        print("ITEM INVENTORY TRACKING PAGE")
        print("===================================")
        print(' 1.Total available quantity of all items sorted in ascending order by Item Code.\n'
                ' 2.Items that has stock quantity less than 25 boxes.\n'
                ' 3.Track available quantity of a specific item\n'
                ' 4.Track item received during a specific time period (startDate to endDate)\n'
                ' 5.Back')
        print("===================================")
        while True:
            choice = (input("Please enter your choice(1,2,3,4 or 5 ): "))
            if not choice:
                print("You can only enter 1 to 5! Please try again.")
            elif not choice.isdigit() or int(choice)<1 or int(choice)>6:
                print("You can only enter 1 to 5! Please try again.")
            else:
                break
        if choice=="1":
            print_available_quantity()
        elif choice =="2":
            reminder()
        elif choice=="3":
            track_available_quantity()
        elif choice == "4":
            find_transactions_range_dates()
        elif choice == "5":
            status = True
            return "back"


#print out all items code and quantity
def print_available_quantity():
    import os
    if not os.path.exists("ppe.txt"):
        print("You cannot print PPE details without PPE file!Please create a file first.")
    else:
        with open("ppe.txt", "r") as ppe:
            lines = ppe.readlines()

            space = "\t" * 3
            horizontal_line = "---" * 23
            print(f"{horizontal_line}\n"
                  f"Item Name{space}Item Code{space}Quantity In stock(boxes)\n"
                  f"{horizontal_line}")
            for line in lines:
                line = line.split(",")
                print(f"{line[0]:<13}{space}{line[1]:<10}{space}{line[3]:>10}")


#track the specific item's quantity
def track_available_quantity():
    with open("ppe.txt","r") as ppe:
        rec_ppe=ppe.readlines()

    while True:
        code=input("Please enter the Item Code you want track:").upper()
        found=False
        for line in rec_ppe:
            if line.split(",")[1]==code:
                found=True
        if not found:
            print("The Item Code you entered doesn't exist.Please try again.")
        else:
            break

    for item in rec_ppe:
        item=item.strip().split(",")
        if item[1]==code:
            print(f"\nCurrent Stock for '{item[1]}' ---->{item[3]}\n")

#track item that has quantity below 25 boxes
def reminder():
    with open("ppe.txt","r") as ppe:
        ppe_rec=ppe.readlines()

    found=False
    for ppe_item in ppe_rec:
        ppe_item=ppe_item.strip().split(",")
        if int(ppe_item[3]) <= 25:
            print(f"\nThe quantity of item {ppe_item[1]} is less than 25 boxes.\n"
                  f"{ppe_item[1]}'s Current Stock Available--->{ppe_item[3]}\n")
            found=True
    if not found:
        print("\nThere is no item's quantity less than 25 boxes\n")



#track item for specific period

def find_transactions_range_dates():
    while True:
        try:
            print("Please enter the STARTING date of tracking the item (Day, Month, Year)")
            start_day = int(input(" a.Day:"))
            start_month = int(input(" b.Month:"))
            start_year = int(input(" c.Year:"))
            start_date_obj = datetime(start_year, start_month, start_day).date()
            start_date = start_date_obj.strftime("%d/%m/%Y")
            print()
            break
        except ValueError as e:
            print("Invalid date input:")
            print("Please enter a valid date.\n")

    while True:
        try:
            print("Please enter the END date of tracking the item (Day, Month, Year)")
            end_day = int(input(" a.Day:"))
            end_month = int(input(" b.Month:"))
            end_year = int(input(" c.Year:"))
            end_date_obj=datetime(end_year,end_month,end_day).date()
            end_date = end_date_obj.strftime("%d/%m/%Y")
            break
        except ValueError as e:
            print("Invalid date input:")
            print("Please enter a valid date.\n")
    if os.path.exists("transaction.txt"):
        with open("transaction.txt","r") as transaction:
            transactions_rec= transaction.readlines()
    else:
        print()
        print("====== IMPORTANT NOTICE ======")
        print("There is no transaction recorded\n")
        return

    space = "\t" * 3
    horizontal_line = "---" * 30
    print(f"{horizontal_line}\n"
          f"Date{space}Item Code{space}Quantity Received(boxes){space}Supplier Code\n"
          f"{horizontal_line}")

    found = False
    for rec in transactions_rec:
        rec=rec.strip().split(",")
        if rec[1]=="Received":
            if start_date <= rec[0] <= end_date:
                found = True
                print(f"{rec[0]:<10}{space}{rec[2]:<10}{space}{rec[4]:>10}{space*2}{rec[3]:>8}")
    print()
    if not found:
        print("The range of the date not founded any transactions ")


#search receive PPE transaction
def search_received_function():
    while True:
        if os.path.exists("transaction.txt"):
            pass
        else:
            print()
            print("====== IMPORTANT NOTICE ======")
            print("There is no transaction recorded\n")
            return

        ItemCode = ['HC', 'FS', 'MS', 'GL', 'GW', 'SC']
        print("Item Code =", ItemCode)
        print()
        choice = input("Please enter the Item Code you want to search:").upper()
        with open("ppe.txt", "r") as ppe:
            lines = ppe.readlines()
        found = False
        for line in lines:
            if line.split(",")[1] ==choice:
                found=True
        if not found:
            print("The Item Code you entered doesn't exist! Please try again.")
        else:
            break

    space = "\t" * 3
    horizontal_line = "---" * 30

    total = 0
    found = False

    with open("transaction.txt") as transaction:
        lines = transaction.readlines()

    for line in lines:
        new_line = line.strip().split(",")
        if new_line[1] == "Received" and new_line[2] == choice:
            if not found:
                print(f"{horizontal_line}\n"
                      f"Date{space}Item Code{space}Supplier Code{space}Quantity Received(boxes)\n"
                      f"{horizontal_line}")
            found = True
            print(f"{new_line[0]:<10}{space}{new_line[2]:<10}{space}{new_line[3]:<10}{space}{new_line[4]:>8}")
            amount = int(new_line[4])
            total += amount

    if found:
        print(f"{horizontal_line}\n"
              f"Total Amount Received{space * 3}{total:>12}")
    else:
        print("There is no transaction for", choice)


#search distributed PPE transaction
def search_distributed_function():
    while True:
        if os.path.exists("transaction.txt"):
            with open("transaction.txt") as transaction:
                lines = transaction.readlines()
        else:
            print()
            print("====== IMPORTANT NOTICE ======")
            print("There is no transaction recorded\n")
            return

        ItemCode = ['HC', 'FS', 'MS', 'GL', 'GW', 'SC']
        print("Item Code =", ItemCode)
        print()
        choice = input("Please enter the Item Code you want to search:").upper()
        with open("ppe.txt", "r") as ppe:
            lines = ppe.readlines()
        found = False
        for line in lines:
            if line.split(",")[1] == choice:
                found = True
        if not found:
            print("The Item Code you entered doesn't exist! Please try again.")
        else:
            break
    if os.path.exists("transaction.txt"):
        with open("transaction.txt") as transaction:
            lines = transaction.readlines()
    else:
        print("There is no transaction recorded\n")
        return

    space = "\t" * 3
    horizontal_line = "---" * 30

    total = 0
    found = False

    for line in lines:
        new_line = line.strip().split(",")
        if new_line[1] == "Distributed" and new_line[2] == choice:
            if not found:
                print(f"{horizontal_line}\n"
                      f"Date{space}Item Code{space}Hospital Code{space}Quantity Distributed(boxes)\n"
                      f"{horizontal_line}")
            found = True
            print(f"{new_line[0]:<10}{space}{new_line[2]:<10}{space}{new_line[3]:<10}{space}{new_line[4]:>8}")
            amount = -int(new_line[4])
            total -= amount

    if found:
        print(f"{horizontal_line}\n"
              f"Total Amount Distributed{space * 3}{total:>8}")
    else:
        print(f"There is no transaction for {choice}\n")


#menu for searching functions
def search_functionalities_menu():
    ItemCode = ['HC', 'FS', 'MS', 'GL', 'GW', 'SC']
    print("===================================")
    print("      Search Functionalities")
    print("===================================")
    print(" (1) Search details of RECEIVED Item\n (2) Search details of DISTRIBUTED Item\n (3) Back")
    print("===================================")
    while True:
        opt=(input("Please enter your choice('1' or '2' or '3'):"))
        if not opt.isdigit() or int(opt)<1 or int(opt)>3:
            print("Your input should be '1' or '2' or '3' only!Please try again")
        else:
            break
    if opt=="1":
        search_received_function()
    elif opt=="2":
        search_distributed_function()
    else:
        return "back"


def ppe_create_file():
    ItemCode=['HC', 'FS', 'MS', 'GL', 'GW', 'SC']
    Item_Name=['Head Cover', 'Face Shield', 'Mask', 'Gloves', 'Gown', 'Shoe Covers']
    Item_Details=zip(ItemCode,Item_Name)
    suppliers={}
    with open("suppliers.txt", "r") as supplier:
        lines = supplier.readlines()

        for line in lines:
            line = line.split(":")
            suppliers[line[0]] = line[1].strip()

    with open("ppe.txt", "w") as ppe:
        for k, j in Item_Details:
            while True:
                opt = input(f"Please enter the supplier code for {k}:").upper()
                if opt not in list(suppliers.values()):
                    print("The supplier doesn't exist!\n")
                else:
                    ppe.write(f"{j},{k},{opt},{100}\n")
                    break

#user can update the specific PPE data
def ppe_update():
    ItemCode=['HC', 'FS', 'MS', 'GL', 'GW', 'SC']
    Item_Name=['Head Cover', 'Face Shield', 'Mask', 'Gloves', 'Gown', 'Shoe Covers']
    Item_Details=zip(ItemCode,Item_Name)
    suppliers = {}
    with open("suppliers.txt", "r") as supplier:
        lines = supplier.readlines()

        for line in lines:
            line = line.split(":")
            suppliers[line[0]] = line[1].strip()

    if not os.path.exists("ppe.txt"):
        print("Please create a PPE file first.")
        record_ppe_menu()
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
                        print("The supplier doesn't exist! Please try again")
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

#menu for PPE
def record_ppe_menu():
    ItemCode=['HC', 'FS', 'MS', 'GL', 'GW', 'SC']
    Item_Name=['Head Cover', 'Face Shield', 'Mask', 'Gloves', 'Gown', 'Shoe Covers']
    Item_Details=zip(ItemCode,Item_Name)
    suppliers={}
    if os.path.exists("suppliers.txt"):
        with open("suppliers.txt","r") as supplier:
            lines=supplier.readlines()

            for line in lines:
                line=line.split(":")
                suppliers[line[0]]=line[1].strip()
    print("===================================")
    print("      PPE ITEMS RECORD SYSTEM")
    print("===================================")
    print(" (1) create PPE file\n (2) update PPE file\n (3) Back")
    print("===================================")
    optioning=True
    while optioning:
        choice=input("Please enter your option number:")
        if choice=="1":
            ppe_create_file()
        elif choice=="2":
            ppe_update()
        elif choice=="3":
            break
        else:
            print("Invalid option!Please try again.")
        choosing = True
        while choosing:
            opt = input("Do you want to stay in 'PPE Item Record System' ('yes' or 'no'):")
            if opt.isalpha():
                if opt=="no":
                    choosing = False
                    optioning=False
                elif opt=="yes":
                    choosing = False
                else:
                    print("You can only enter 'yes' or 'no'.")
            else:
                print("You can only enter 'yes' or 'no'.")
    print("Command executed successfully")


#record all 3 suppliers' details
def record_supplier_detail():
    suppliers = {}
    code_list=[]
    with open("suppliers.txt", "w") as supplier:
        for i in range(3):
            while True:
                supplier_name = input(f"Please enter the name of supplier {i+1}:")
                if not supplier_name:
                    print("The supplier cannot be empty")
                else:
                    break

            while True:
                supplier_code = input(f"Please give '{supplier_name}' a supplier code (2 characters):").upper()
                print()
                if len(supplier_code)!=2:
                    print("Your supplier code can only be 2 characters")
                elif supplier_code in code_list:
                    print(f"The supplier code for '{supplier_name}' is same with others!Please try another code. ")
                else:
                    code_list.append(supplier_code)
                    break

            suppliers[supplier_name] = supplier_code
        for key, value in suppliers.items():
            supplier.write(f"{key}:{value}\n")
    print("Suppliers File has been created successfully!")

#print out supplier's detail
def print_supplier():
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


#menu for user to manage suppliers' details
def record_suppliers_menu():
    optioning=True
    while optioning:
        print("===================================")
        print(" Suppliers' Detail Record System")
        print("===================================")
        print(" (1) Record Suppliers' Details\n (2) Print out supplier details\n (3) Back")
        print("===================================")
        choice=input("Please enter your option number:")
        if choice=="1":
            record_supplier_detail()
        elif choice=="2":
            print_supplier()
        elif choice=="3":
            break
        else:
            print("Invalid option.Please try again")

        choosing=True
        while choosing:
            opt=input("Do you want to continue  ('yes' or 'no'):")
            if opt.isalpha():
                if opt=="no":
                    choosing=False
                    optioning=False
                elif opt=="yes":
                    choosing=False
                else:
                    print("You can only enter 'yes' or 'no'.")
            else:
                print("You can only enter 'yes' or 'no'.")
    print("Command executed successfully")


#create and renew hospital.txt
def create_hospital():
    with open("hospital.txt", "w") as hospital:
        previous_code=[]
        for i in range(3):
            while True:
                name=input(f"Please enter the name of Hospital {i+1}:")
                if not name:
                    print("The Hospital name cannot be empty.")
                else:
                    break

            while True:
                code=input(f"Please enter the code of Hospital {i+1} (2 characters):").upper()
                if len(code)!=2:
                    print("The hospital code should be 2 characters only!Please try again\n")
                elif code in previous_code:
                    print(f"The Hospital {i+1} code is same with others!Please try another code.\n")
                else:
                    previous_code.append(code)
                    break
            print()
            hospital.write(f"{name},{code}\n")
        print()
    print("Hospital file created successfully!")

#update hospital data
def update_hospital():
    if os.path.exists("hospital.txt"):
        s = True
        while s:
            with open("hospital.txt","r") as hospital:
                lines=hospital.readlines()
            opt = input("Please enter the hospital code you want to update:").upper()
            found = False
            for i,line in enumerate(lines):
                if line.split(",")[1].strip()==opt:
                    found=True

                    while True:
                        updated_name=input("Please enter the UPDATED hospital name:")
                        if not updated_name:
                            print("The hospital name cannot be empty")
                        else:
                            break

                    while True:
                        updated_code=input("Please enter the UPDATED hospital code (2 characters):").upper()
                        code = []
                        for line in lines:
                            code.append(line.split(",")[1].strip())
                        if updated_code in code:
                            print("The hospital have already exists.Please try another code.")
                            continue

                        if len(updated_code)!=2:
                            print("The Hospital Code should be 2 characters")
                        else:
                            break
                    updated_line=f"{updated_name},{updated_code}\n"
                    lines[i]=updated_line

                    with open("hospital.txt","w") as hospital:
                        hospital.writelines(lines)
                        print("Hospital details successfully updated")
                        s = False

            if not found:
                print("The hospital doesn't exist!Please try again.")

    else:
        print("You must create a hospital details file first!")

#menu for user to manage hospital data
def hospital_menu():
    optioning=True
    while optioning:
        print("===================================")
        print("     Record Hospital System")
        print("===================================")
        print(" (1) create Hospital File\n (2) update Hospital File\n (3) Back")
        print("===================================")
        choice = input("Please enter your option number:")
        if choice == "1":
            create_hospital()
        elif choice == "2":
            update_hospital()
        elif choice == "3":
            optioning=False
            break
        else:
            print("Invalid option.Please try again")

        choosing = True
        while choosing:
            opt = input("Do you want to stay in 'Record Hospital System' ('yes' or 'no'):")
            if opt.isalpha():
                if opt == "no":
                    choosing = False
                    optioning=False
                elif opt=="yes":
                    choosing=False
                else:
                    print("You can only enter 'yes' or 'no'.")
            else:
                print("You can only enter 'yes' or 'no'.")
    print("Command executed successfully")

#menu that allows user to manage "ppe.txt","suppliers.txt" and "hospital.txt"
def file_management():
    while True:
        print("===================================")
        print("     File Management System")
        print("===================================")
        print(" (1) PPE file\n (2) Supplier File\n (3) Hospital File\n (4) Back")
        print("===================================")
        choice = input("Please enter your option number:")
        if choice == "1":
            record_ppe_menu()
        elif choice == "2":
            record_suppliers_menu()
        elif choice == "3":
            hospital_menu()
        elif choice=="4":
            break
        else:
            print("Invalid option.Please try again")
    return "back"

#Initial file creation when first time running this program
def initial_file_creation():
    print("===================================")
    print("  Initial File Creation System")
    print("===================================")
    print(" (1)Creation of 'suppliers.txt'")
    record_supplier_detail()
    print("===================================")
    print(" (2)Creation of 'ppe.txt'")
    ppe_create_file()
    print("===================================")
    print(" (3)Creation of 'hospital.txt'")
    create_hospital()
    print()


#Main Interface
print('     Welcome to Inventory Management System'.title())
print("The first user who uses our system will be a default admin\n")
logging_in=True
while logging_in:
    while True:
        user_ID=input("Please enter your User ID:")
        if user_ID.isdigit() and len(user_ID)==4:
            break
        else:
            print("User ID should be 4-digit numbers")

    while True:
        user_name=input("Please enter your User name:").lower()
        if not user_name:
            print("Your name cannot be empty")
        else:
            break
    while True:
        user_password=input("Please enter your User Password:")
        if len(user_password) < 8 or len(user_password) > 16:
            print("User's password should be 8-16 characters!")
        else:
            break
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as user:
            user.write(f"{user_ID},{user_name},{user_password},admin\n")

    with open("user.txt","r") as user:
        lines=user.readlines()

        i=0
        for line in lines:
            split_line=line.split(",")
            if user_ID==split_line[0] and user_name==split_line[1] and user_password==split_line[2]:
                print("Successfully logged in\n")
                logging_in = False
                break
        if logging_in==True:
            print("Invalid User's Information.Please retry\n")

if not (os.path.exists("ppe.txt") and os.path.exists("suppliers.txt") and os.path.exists("hospital.txt")):
    print("                         =========== IMPORTANT NOTICE===========")
    print("Please complete the creation of 'ppe.txt', 'suppliers.txt', 'hospital.txt' before making further operation.\n")
    initial_file_creation()
    print("All files created successfully.")

print("Entering user interface... PLease wait")
time.sleep(1)

if split_line[3].strip()=="admin":
    while True:
        result1,result2,result3,result4=admin()
        if result1 == "back" or result2 == "back" or result3 == "back" or result4 == "back":
            result1, result2, result3, result4 = admin()
        else:
            break
if split_line[3].strip() == "staff":
    while True:
        result1, result2, result3, result4 = staff()
        if result1 == "back" or result2 == "back" or result3 == "back" or result4 == "back":
            staff()
        else:
            break
