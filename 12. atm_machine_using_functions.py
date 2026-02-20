'''1. need to give intro
   2. need to insert card
   3. need to get account number
   4. need to confirm with atm pin
   5. need to clarify the pin and if its wrong give 3 attempts to correct
   6. run the options in loop
   7. option for change pin?'''

name = ['Rohit','Mehul','Manan']                                            #pre-defining the details of users
pin = [2000,2006,2012]
account_number = [123422347654,765498762953,635492166543]                   #account number will be the differentiating factor between users as name and pin might be same
account_balance = [100000,150000,200000]

#------------------------------------------------------------#
intro_1 = 'Welcome, Please insert your card.'
intro_2 = 'Do not remove your card during the transaction'
lines_length_1 = len(intro_1)
lines_length_2 = len(intro_2)
line_length = max(lines_length_1, lines_length_2)
for x in range(line_length):
    print('-',end = '')
print(f'\n{intro_1}')
print(intro_2)
print('\nEnter your account number')
for x in range(line_length):
    print('-', end = '')
print('\n')
#------------------------------------------------------------#

user_account_number = int(input('Account number: '))                        #to identify the user
acc_check = account_number.__contains__(user_account_number)                #checks whether the account number entered is valid or not
if acc_check == True:
    user_index = account_number.index(user_account_number)                  #this gives us the index and the details of the user
    
    a = 0
    b = 0
    while a!=1:
        while b!=3:                                                             #until correct pin is entered
            user_pin = int(input('Enter your pin'))                             #to confirm the user
            if user_pin == pin[user_index]:
                b = 3
                a += 1
                print(f'Welcome {name[user_index]}!')

                print("1. Withdrawal")
                print("2. Quick cash")
                print("3. Balance Inquiry")
                transaction_type = int(input('Enter serial number of transaction you want to perform: '))

                def withdrawal():                                   
                    amount = int(input('Enter amount to be withdrawn(multiple of 100s)'))
                    if amount%100 == 0:
                        print('Withdrawal successful')
                        account_balance[user_index] -= amount
                        print(f'Available balance = {account_balance[user_index]}')
                    else:
                        print('Invalid amount')

                def quick_cash():
                    print('1. 1000, 2.5000, 3. 10000, 4. 20000')
                    amount = int(input('Enter amount '))
                    print('Withdraw successful')
                    account_balance[user_index] -= amount
                    print(f'Available balance = {account_balance[user_index]}')

                def acc_bal():
                    print(f'Available balance = {account_balance[user_index]}')

                if transaction_type == 1:
                    withdrawal()

                if transaction_type == 2:
                    quick_cash()

                if transaction_type == 3:
                    acc_bal()

            else:
                print('Wrong pin entered.')
                b += 1
    if b == 3:
        print("No attempts left.")

else:
    print('Invalid account number. Try again!')