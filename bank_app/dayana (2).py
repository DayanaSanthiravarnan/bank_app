#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_create_first_admin-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

import os
from colorama import Fore, Back,Style,init
init(autoreset=True)

def create_customer_next_id():
    if not os.path.exists("customer.txt") or os.path.getsize("customer.txt") == 0:
        return "C001"
    with open("customer.txt", "r") as customer_file:        
        return f"C{int(customer_file.readlines()[-1].split(',')[0][1:]) + 1:03}"

def create_user_next_id():
    if not os.path.exists("user.txt") or os.path.getsize("user.txt") == 0:
        return "U001"
    with open("user.txt", "r") as user_file:        
        return f"U{int(user_file.readlines()[-1].split(',')[0][1:]) + 1:03}"
    
def create_first_admin():
    if not os.path.exists("user.txt") or os.path.getsize("user.txt") == 0:
        adminname ="dayana05"
        adminpassword ="dayana@123"
        with open("user.txt" , "a") as user_file:
            user_file.write(f"{create_user_next_id()},{adminname},{adminpassword},Admin\n")
        print('Admin Login Details: Username: ', adminname, 'Password: ',  adminpassword)
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-




#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_customer_info-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


def customer_info():
    while True:
        try:
            username = input("\nPlease enter customer username: ")
            user = False
            with open("user.txt" , "r") as user_file:
                for line in user_file:
                    parts = line.strip().split(",")
                   
        
                    if username == parts[1]:
                       user = True
            if user:
                    print( "your username already exit ." "Re enter your username !" )
                                
            else:
                print( "successful!" )
                break
                        
        except FileNotFoundError:
            print(Fore.RED+Style.BRIGHT+"file not found .")
           
    while True:

            password = input("(Password must be 8 characters! ) Enter customer password: ")
            if len(password) >= 8 :
                break                
            else:
                print(Fore.RED+Style.BRIGHT+"Password must be 8 characters !" "Please try again")

    name = input("Enter customer name: ")
    
    while True:
        NIC_NO =input("Enter customer NIC NO: ")
        if len(NIC_NO) <= 12: 
            

            break
        else:
            print("Re enter your NIC number !")

    while True:
        try:    
            age = int(input("Enter customer age : "))
            if age <= 69:
                break
            else:
                print(Fore.RED+Style.BRIGHT+"Re enter your  age !")
        except ValueError:
            print(Fore.RED+Style.BRIGHT+"Enter numbers only!")

    while True :
        try:   
            print("Male     :male" )
            print("Female   :female")
            gender =input("Enter your number :")
            
            if gender =="male":
                
                break
            elif gender =="female":
                
                break
            else:
                print(Fore.RED+Style.BRIGHT+"Invalid choice")
        except ValueError :
            print(Fore.RED+Style.BRIGHT+"Enter number only!")
            
    address = input("Enter customer address : ")
    while True:
        try:
            Phone_No = int(input('Enter customer phone number :'))
            

            break
           
            
        except ValueError:
            print(Fore.RED+Style.BRIGHT+"Enter numbers only!")

    
    return {
            "username": username,
            "password": password,   
            "name":name,
            "NIC_NO":NIC_NO,
            "age":age,
            "gender":gender,
            "address":address,
            "Phone_No":Phone_No
            }
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


def create_customer_and_user():
    customer = customer_info()
    

    with open("customer.txt", "a") as customer_file, open("user.txt", "a") as user_file:
        customer_file.write(f"{create_customer_next_id()},{customer["name"]},{customer["NIC_NO"]},{customer["age"]},{customer["gender"]},{customer["address"]},{customer["Phone_No"]}\n")
        user_file.write(f"{create_user_next_id()},{customer["username"]},{customer["password"]},{create_customer_next_id()}\n")
        print(Fore.CYAN+Style.BRIGHT+"\ncustomer id :",create_customer_next_id() ,'Name :' ,customer["name"])
 

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ Create_New_Account-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


import os
from datetime import datetime

def Create_New_Account():
    id_number = input("\nEnter customer ID number: ")


    
    try:
        with open("customer.txt", "r") as customer_file:
            for line in customer_file:
                id_NO = line.strip().split(",")
                if id_NO[0] == id_number:
                    
                    break  
    except FileNotFoundError:
        print(Fore.RED+Style.BRIGHT+"\nCustomer file not found.")

    if not id_number:
        print(Fore.RED+Style.BRIGHT+"\nCustomer with ID" ,id_number, "not found. Please create a customer.")
        return 

   
    account_num = 1000 
    count = 0

    try:
        with open("account_no.txt", "r") as account_file:
            
            for _ in account_file:
                count += 1 
    except FileNotFoundError:
        pass  

    new_account_no = account_num + count

   
    try:
        with open("account_no.txt", "a") as account_file:
           
            ac_balance = float(input("\n(Please deposit only 600 =< !) Enter your initial deposit money :"))
            if ac_balance >= 600:

                print(Fore.CYAN+Style.BRIGHT+"\nNew account created with Account No:", new_account_no ,"Your balance is RS.", ac_balance)
                date_time = datetime.now().strftime('%d-%m-%Y %A %I:%M %p')
                correct_balance = ac_balance

                with open("transaction.txt",'a') as file:
                    file.write(f"{new_account_no},{correct_balance},Deposit,{correct_balance},{date_time}\n")
            else:
                print("\nPlease deposit only 600 =< !")
            account_file.write(f"{id_number},{new_account_no},{correct_balance}\n")
            
        
    except Exception :
        print(Fore.RED+Style.BRIGHT+"\nError writing to account_no.txt: ")

    return str(new_account_no)

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_balance-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


def balance():
    account_number = input("Enter your account number:")
    try:
        with open("account_no.txt" , "r") as account_file:
            for line in account_file:
                parts = line.strip().split(",")
                if account_number == parts[1]:
                    balance = float(parts[-1])
                    print("Account number available !""your balance is",balance)
                    break
                    

            else:
                print(Fore.RED+Style.BRIGHT+f"\nAccount number : {account_number} not found.")
    except FileNotFoundError:
        print(Fore.RED+Style.BRIGHT+"account file not found")
    


import os
from datetime import datetime
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_amount-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


def amount():
    while True:
        try:
            amt = float(input("\nEnter amount: "))
            if amt >= 0:
                
                return amt
            else:
                print("Enter invalid amount!" )
        except ValueError:
            print(Fore.RED+Style.BRIGHT+"\nInvalid input. Please enter a valid amount.")

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-deposit_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

import os
from datetime import datetime
def deposit():
    acc_no = input("\nenter customer account number :").strip()
    try:
        
        with open("account_no.txt" , "r") as account_file:
            for line in account_file:
                parts = line.strip().split(",")
                if acc_no == parts[1]:
                    balance = float(parts[-1])
                    deposit_amount = amount()
                    new_balance = balance + deposit_amount
                    with open("account_no.txt" , "w") as account_file:
                        account_file.write(f"{parts[0]},{parts[1]},{new_balance}\n")
                    date_time = datetime.now().strftime('%d-%m-%Y %A %I:%M %p')
                    with open("transaction.txt" , "a") as transaction_file:
                        transaction_file.write(f"{acc_no},{balance},Deposit,{deposit_amount},{date_time}\n")
                        print(Fore.CYAN+Style.BRIGHT+"\nDeposit successful! Your current balance is:", new_balance)
                        print(Fore.CYAN+Style.BRIGHT+"\naccount number :",acc_no,  "|"   "Deposit amount :",deposit_amount,   "|"  "Deposit time   :" ,date_time )
                        
                        break

            else:
                print("account number:",acc_no ,"not found!")

    except FileNotFoundError:
        print("account file not found!")

                






import os
from datetime import datetime
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_Withdraw-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


def Withdraw():
    ac_no = input("Enter your account number :")
    try: 
        with open("account_no.txt" , "r") as account_file:
            for line in account_file:
                parts = line.strip().split(",")
                if ac_no == parts[1]:  
                    
                    balance = float(parts[-1])
                    
                    withdraw = amount()
                    if balance >= withdraw:
            
                        new_balance = balance - withdraw
                        date_time = datetime.now().strftime('%d-%m-%Y %A %I:%M %p')
                        with open("account_no.txt" , "w") as account_file:
                            account_file.write(f"{parts[0]},{parts[1]},{new_balance}\n")
                        with open("transaction.txt","a") as transaction_file:
                            transaction_file.write(f"{ac_no},{balance},Withdraw,{withdraw},{date_time}\n")
                            print(Fore.CYAN+Style.BRIGHT+"\nWithdrawal successful! Your current balance is:", new_balance)

                            print(Fore.CYAN+Style.BRIGHT+"\naccount number :",ac_no,  "|"   "Withdraw amount :",withdraw,   "|"  "Withdraw time   :",date_time )
                            break
                    else:
                        print(Fore.RED+Style.BRIGHT+"your balance is not enough!")
                else:
                    print(Fore.RED+Style.BRIGHT+"account number:",ac_no ,"not found!")

    except ValueError:
        print(Fore.RED+Style.BRIGHT+"file not found!")




#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-view_account_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
def view_account():
    account_number = input("\nEnter your account number :")
    try:
        with open("account_no.txt" , "r") as account_file:
            for line in account_file:
                a_line = line.strip().split(",")
                if account_number == a_line[1]:
                    with open("customer.txt ", "r") as customer_file:
                        for i in customer_file:
                            c_i = i.strip().split(",")
                            if a_line[0] == c_i[0]:
                                print(Fore.CYAN+Style.BRIGHT+f"\n Account Number        :{a_line[1]}")
                                print(Fore.CYAN+Style.BRIGHT+f"Customer id             :{c_i[0]}") 
                                print(Fore.CYAN+Style.BRIGHT+f"Name                    :{c_i[1]}")
                                print(Fore.CYAN+Style.BRIGHT+f"NIC_N0                  :{c_i[2]}")
                                print(Fore.CYAN+Style.BRIGHT+f"Age                     :{c_i[3]}")
                                print(Fore.CYAN+Style.BRIGHT+f"Gender                  :{c_i[4]}")
                                print(Fore.CYAN+Style.BRIGHT+f"Address                 :{c_i[5]}")
                                print(Fore.CYAN+Style.BRIGHT+f"Phone_No                :{c_i[6]}\n")   
                            
                            
        
                else:
                    print(Fore.RED+Style.BRIGHT+"\ncustomer account number not found !")

    except FileNotFoundError:
        print(Fore.RED+Style.BRIGHT+"\nfile not found !")


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_transaction_history-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

def transaction_history():
    acc_no = input("\nEnter your account number: ")
    found = False
    try:
        with open("transaction.txt", "r") as transaction_file:
            print(f"{'Ac_No':<10}{'last balance':<15}{'Action':<10}{"amount":<15}{"date":<20}{"time":<15}\n ")
            for trans_line in transaction_file:
                trans_data = trans_line.strip().split(",")
                if acc_no == trans_data[0]:
                    print(Fore.CYAN+Style.BRIGHT+f"{trans_data[0]:<10}{trans_data[1]:<15}{trans_data[2]:<10}{trans_data[3]:<20}{trans_data[4]:<15}\n")
                    found = True
                
                    
            if not found:
                print(Fore.RED+Style.BRIGHT+"System Too Busy !, Please Try Later")
            
    except FileNotFoundError:
        print(Fore.RED+Style.BRIGHT+"\nTransaction file not found.")
    

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_update-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


               
def update():
    customer_id = input("Enter customer id number: ")
    lines = []
    customer_found = False 
    try:
        with open("customer.txt", "r") as customer_file:
            lines = customer_file.readlines()

        
        with open("customer.txt", "w") as customer_file:
            for line in lines:
                up_line = line.strip().split(",") 
                
                
                if up_line[0] == customer_id:
                    customer_found = True
                    while True:
                        print(Fore.YELLOW+Style.BRIGHT+"\n====== MENU ======")
                        print("1. Change name")
                        print("2. Change NIC number")
                        print("3. Change age")
                        print("4. Change gender")
                        print("5. Change address")
                        print("6. Change phone number")
                        print("7. Exit")

                        try:
                            choice = int(input("\nEnter your choice: "))
                        except ValueError:
                            print(Fore.RED+Style.BRIGHT+"\nInvalid input! Please enter a number.")
                            continue

                        if choice == 1:
                            up_line[1] = input(f"\nEnter new name (Current: {up_line[1]}): ")
                        elif choice == 2:
                            up_line[2] = input(f"Enter new NIC number (Current: {up_line[2]}): ")
                        elif choice == 3:
                            up_line[3] = input(f"Enter new age (Current: {up_line[3]}): ")
                        elif choice == 4:
                            up_line[4] = input(f"Enter new gender (Current: {up_line[4]}): ")
                        elif choice == 5:
                            up_line[5] = input(f"Enter new address (Current: {up_line[5]}): ")
                        elif choice == 6:
                            up_line[6] = input(f"Enter new phone number (Current: {up_line[6]}):\n")
                        elif choice == 7:
                            break  
                        else:
                            print(Fore.RED+Style.BRIGHT+"\nInvalid number! Please try again.")

                    
                    customer_file.write(",".join(up_line) + "\n")
                else:
                    
                    customer_file.write(line)

        if not customer_found:
            print(f"\nCustomer with ID {customer_id} not found!")
        else:
            print("\nCustomer details updated successfully.")

    except FileNotFoundError:
        print(Fore.RED+Style.BRIGHT+"\ncustomer_file not found")



    





#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-customer_password_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

def customer_password():
    customer_id = input("\nEnter your customer ID :")
    while True:
        try:
            with open("user.txt" , "r") as user_file:
                for line in user_file:
                    U_line = line.strip().split(",")
                    if customer_id == U_line[-1]:

                        user_name = input("Enter your username :" )
                        pass_word = input("Enter your password :" )
                        if user_name == U_line[1] and pass_word == U_line[2]:
                            print("\nSuccessful login!")
                            return True
                            
                        else:
                            print(Fore.RED+Style.BRIGHT+"\nUnsuccessful login. Please try again.")
                            return False
                
        except FileNotFoundError:
            print(Fore.RED+Style.BRIGHT+"\nfile not found")
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
import os
from datetime import datetime
def Current_date():
    date_time = date_time = datetime.now().strftime("%Y-%m-%d ")
    print("current Date :",date_time)


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
def transaction_summary():
    acc_no = input("Enter your account number :")
    count_deposit = 0
    count_withdraw = 0

    try:
        with open("transaction.txt ", "r") as transaction_file:
            for line in transaction_file:
                parts = line.strip().split(",")
                if acc_no == parts[0] and len(parts) >= 4:
                    if parts[2] =="Deposit": 

                        count_deposit += 1
                    elif parts[2] =="Withdraw":
                        count_withdraw += 1
            else:
                print("account number not found")
        print("Total deposit     :",count_deposit)
        print("Total withdraw    :",count_withdraw)
                
    except FileNotFoundError:
        print("file not found!!!")


        

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_admin-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


def admin():
    while True:
            
        create_first_admin()
        a_name = input("\nEnter your username: ")
        a_password = input("Enter your password:")
        
        if True:   
            
            try:
                with open("user.txt", "r") as user_file:
                    for line in user_file:
                        fields = line.strip().split(",")
                        if fields[-1] == "Admin":
                            username = fields[1]
                            password = fields[2]

                            if username == a_name and password == a_password:
                                print("\nSuccessful login!")

                            
                                try:
            
                                    while True:
                                        print(Fore.YELLOW+Style.BRIGHT+"\n----Admin Menu----")
                                        print("\nCreate New User              : 101")
                                        print("Create New Account           : 102")
                                        print("Deposit Amount               : 103 ")
                                        print("Withdraw Money               : 104")
                                        print("Check Balance                : 105")
                                        print("View Account                 : 106")
                                        print("transaction History          : 107")
                                        print("Changes or Update Account    : 108")
                                        print("currente date                : 109")
                                        print("transaction_summary          : 110")
                                        print("Exit                         : 111\n" )

                                        
                                        Choice = int(input("Enter your choice :"))
                            
                                        if Choice == 101:
                                            create_customer_and_user()
                                        elif Choice == 102:
                                            Create_New_Account()
                                        elif Choice == 103:
                                            deposit()
                                        elif Choice == 104:
                                            Withdraw()
                                        elif Choice == 105:
                                            balance()

                                        elif Choice == 106:
                                            view_account()
                                        elif Choice == 107:
                                            transaction_history()
                                        elif Choice == 108:
                                            update()
                                       
                                        elif Choice == 109:
                                            Current_date()
                                        elif Choice == 110:
                                            transaction_summary()
                                        elif Choice == 111:
                                            print("\nThank you")
                                            exit()
                                        else:
                                            print("\ninvalid number! try again.")
                            

                                except ValueError:
                                    print(Fore.RED+Style.BRIGHT+"\nInvalid choice please enter a number")
                    else:
                        print(Fore.RED+Style.BRIGHT+"\nUnsuccessful login. Please try again.")


                            

            except FileNotFoundError:
                        print(Fore.RED+Style.BRIGHT+"\nUser file not found.")

                                

# #_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_customer-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    

def customer():
        if True:
            U_P = customer_password()
            if U_P == True:
                while True:
                    print(Fore.YELLOW+Style.BRIGHT+"\n----Customer Menu----")
                    print("\nDeposit Amount           : 1 ")
                    print("Withdraw Money           : 2")
                    print("Check Balance            : 3")
                    print("View Account             : 4 ")
                    print("transaction History      : 5")
                    print("Exit                     : 6\n" )
                    



                    try:
                        Choice = int(input("\nEnter your choice :"))
                        if Choice == 1:
                            deposit()

                        elif Choice == 2:
                            Withdraw()

                        elif Choice == 3:
                            balance()
                        elif Choice == 4:
                            view_account()
                        elif Choice == 5:
                            transaction_history()
                        elif Choice == 6:
                            print("\nThank you!")
                            break
                        else:
                            print(Fore.RED+Style.BRIGHT+"\nInvalid Number!")
                    except ValueError:
                        print(Fore.RED+Style.BRIGHT+"\nInvalid choice please enter a number")
            
            else:
                print("try again!!!")
#-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-        
while True:
    
    print(Fore.YELLOW+"\n----Are you customer or admin----")
    print("You are admin Enter number           : 1")
    print("You are customer Enter number        : 2")
    print("Exit                                 : 3\n")
    
    
    try:
        Select = int(input("\nEnter your choice :"))
        if Select ==1:
            admin()
        elif Select ==2:
            customer()
            
        elif Select ==3:
            print("Thank you !")
            break
        else:
            print(Fore.RED+Style.BRIGHT+"\ninvalid number!" "Try again" )
    except ValueError:
        print(Fore.RED+Style.BRIGHT+"\nInvalid choice please enter a number")

