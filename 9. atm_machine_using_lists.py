name = ['Mehul','Manan']
pin = [2006,2012]
acc_bal = [200000,100000]

print(pin.__contains__(2006))

print('Welcome insert your card!')
application_id = input("Enter the type of transaction you want to do (domestic/international)")
application_id = application_id.lower()
if application_id == 'domestic':
    language = input('Enter your preferred language (english/hindi)')
    language = language.lower()

    user_pin = int(input('Enter your pin'))           #making the user enter their pin to identify them, name cant be used as it may repeat with another person
    user_index = pin.index(user_pin)        #how to print invalid pin 

    print('1. Net Banking')
    print('2. Withdrawal')
    print('3. Quick Cash')
    print('4. Balance Inquiry')
    print('Welcome ',name[user_index])
    transaction_type = int(input('Enter the serial number of transaction you want to perform'))

    user_input = 'Y'
    while user_input == 'Y':

        if transaction_type == 1:
            acc_num = input('Enter bank account number of other person')
            if len(acc_num) == 14:
                amount = int(input("Enter amount to be transferred"))
                print('Transaction successful')
                acc_bal[user_index] -= amount
                print('Available balance: ',acc_bal[user_index])
            else:
                print('Invalid account number')

        if transaction_type == 2:
            amount = int(input('Enter amount to be withdrawn(multiple of 100)'))
            if amount%100 == 0:
                print('Withdrawal successful')
                acc_bal[user_index] -= amount
                print('Avaialable balance = ',acc_bal[user_index])
            else:
                print('Invalid amount')

        if transaction_type == 3:
            print('1. 1000; 2. 5000; 3. 10000; 4. 20000 ')
            amount = int(input('Enter amount to be withdrawn'))
            print('Withdraw successful')
            acc_bal[user_index] -= amount
            print('Available balance: ',acc_bal[user_index])

        if transaction_type == 4:
            print('Available balance: ',acc_bal[user_index])

        user_input = input("Want to do another transaction(Y/N)")
        

else:
    print('International transactions not available currently')