
"""
# Q. ATM Machine Simulation
#
# Write a Python program to simulate an ATM machine with the following rules:
#
# 1. PIN Verification:
#    - Default correct PIN is 1234.
#    - User gets a maximum of 3 attempts to enter the correct PIN.
#    - If entered incorrectly 3 times, print "Card Blocked! Please contact your bank." and terminate.
#
# 2. Main Menu (runs continuously until user exits):
#    - Initial Account Balance = ₹5000. 
#    - If PIN is correct, show the menu options:
#        1. Check Balance
#        2. Deposit Cash
#        3. Withdraw Cash
#        4. Exit
#
# 3. Operations:
#    - Option 1: Display the current balance.
#    - Option 2: Ask for deposit amount, add it to balance, and display updated balance.
#    - Option 3: Ask for withdrawal amount.
#                If amount <= balance, deduct and print "Withdrawal Successful".
#                Otherwise, print "Insufficient Balance!".
#    - Option 4: Print "Thank you for using our ATM. Have a nice day!" and exit the loop.
#    - Any other option: Print "Invalid Choice! Please choose 1 - 4."
"""

"""
user ki attemps ke ander pin check krna hai 
user se pin check krna hai in limits -> pin_real == pin_input
-> incorrect
-> 1st time and 2nd and -> pin is incorrect -> chance dena again
-> 3rd time -> incorrect -> card blocked chor ho appp
1st and 2nd and 3rd ->correct -> main menu and chance stop 
main menu (1,2,3,4)
balance = 5000 +1000-2000

""" 


# input should be taken when user have left out attempts

# attempts =3
# has_access_mainmenu = False
# """ this logic is for checking wheather user have entered pin correct or not"""
# while attempts > 0:
#     entered_pin = int(input("enter the pin"))
#     if entered_pin == 1234:
#         # main menu openes
#         has_access_mainmenu = True
#         break
#     else:
#         attempts -=1
#         if attempts>0:
#             print(f"incorrect pin! you have {attempts} attempts remaining")
#         else:
#             print("card blocked")
            
# balance = 50000
# if has_access_mainmenu == True:
#     while True:
#         print("ATM Menu")
#         print("1 -> check balance")
#         print("2 -> deposit cash")
#         print("3-> withdraw cash")
#         print("4->exit")
        
#         choice = int(input("enter the choice"))
        
#         if choice == 1:
#             print(f"Balance is {balance} only")
#         elif choice ==2:
#             depoist_amount = int(input("enter the ammount to deposit"))
#             if depoist_amount > 0:
#                 balance +=depoist_amount
#                 print(f"updated balance is {balance}")
#             else:
#                 print("invalid depoist ammount")
#         elif choice ==3:
#             withdraw_ammount = int(input("enter the ammount to withdraw"))
#             if withdraw_ammount <=balance:
#                 balance-=withdraw_ammount
#                 print(f"withdraw done and updated balance is {balance}")
#             else:
#                 print("insufficient balance")
#         elif choice ==4:
#             print("thank you for using our atm")
#             break
#         else:
#             print("invalid choice ! please enter number from 1 - 4")




# attempt = 3
# acces_main_menu = False
# while attempt > 0:
#     enter_pin = int(input("enter the pin :-"))
#     if enter_pin == 1234:
#         acces_main_menu = True
#         break
#     else:
#         attempt -= 1
#         if attempt > 0:
#             print(f"incorrect pin u have only {attempt} remaining attempt")
#         else:
#             print("card block")
# balance = 100000
# if acces_main_menu == True:
#     while True:
#         print("1->  check balance")
#         print("2->  deposite cash")
#         print("3->  withdraw cash")
#         print("4->  Exit")

#         choice = int(input("enter the choice :"))

#         if choice == 1:
#             print(f"the available balance is {balance}")
#         elif choice == 2:
#             deposite_amount = int(input("enter the amount :"))
#             if deposite_amount > 0:
#                 balance += deposite_amount
#                 print(f"updated balance is {balance}")
#             else:
#                 print("invalid deposite amount")
#         elif choice == 3:
#             withdraw_amount = int(input("enter the amount for withdraw cash :"))
#             if withdraw_amount <= balance:
#                 balance -= withdraw_amount
#                 print(f"wihdraw done and updated balance is {balance}")
#             else:
#                 print("insuficient balance")
#         elif choice == 4:
#             print("thanku for visiting")
#             break
#         else:
#             print("invalid choice ! please enter the number from 1 to 4")