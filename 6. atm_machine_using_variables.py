pin_code = 2006                                                          #pre-set ATM pin
acc_bal = 250000                                                         #pre-set balance

print("Welcome! Insert your card")
application_id = input("Enter application ID : Domestic/International ")        #opting nature of transaction
application_id = application_id.lower()
if application_id == 'domestic':
    language = input("Select Language : English/Hindi ")                 #Selecting Language
    language = language.lower()                                          #incase user enters the word in diff caps(as python is case sensitive)
    
    user_input = 'Y'
    while user_input == 'Y':                                             #running in loop
        print("1. Net banking")
        print("2. Withdrawal")
        print("3. Quick cash")
        print("4. Balance Inquiry")
        transaction_type = int(input("Enter serial nummber of transaction you want to perform "))            #selecting type of transaction to be performed

        if transaction_type == 1:
            pin_num = int(input("Enter the 4-digit ATM pin "))
            if pin_num == pin_code:                                                     #how to use continue function here
                acc_num = input("Enter bank account number of other person ")
                if len(acc_num) == 14:
                    amount = int(input("Enter amount to be transferred "))
                    print("Transaction successful")
                    acc_bal -= amount                                                   #Updated balance
                    print("Available balance = ",(acc_bal))
                else:
                    print("Invalid account number")
            else:
                print("Wrong pin")

        if transaction_type == 2:
            pin_num = int(input("Enter the 4-digit ATM pin "))
            if pin_num == pin_code:
                amount = int(input("Enter amount to be withdrawn(Multiple of 100) "))
                if (amount%100 == 0):
                    print("Withdrawal successful")
                    acc_bal -= amount
                    print("Available balance = ",(acc_bal))
                else:
                    print("Invalid amount")
            else:
                print("Wrong pin")

        if transaction_type == 3:
            pin_num = int(input("Enter the 4-digit ATM code"))
            if pin_num == pin_code:
                print("Select the amount to be withdrawn")
                print("1. 1000, 2. 5000, 3. 10000, 4. 20000")
                amount = int(input("Enter amount "))
                print("Withdraw successful")
                acc_bal -= amount
                print("Available balance = ",(acc_bal))
            else:
                print("Wrong pin")

        if transaction_type == 4:
            pin_num = int(input("Enter the 4-digit ATM code "))
            if pin_num == pin_code:
                print("Your account balance is: ",(acc_bal))
            else: 
                print("Wrong pin")
        
        user_input = input("Want to do another transaction(Y/N)")


else:
    print("International transfers not available currently")
