#------------------------------------------------------------|
intro_1 = 'Welcome, Please insert your card.'                #
intro_2 = 'Do not remove your card during the transaction'   #
                                                             #
lines_length_1 = len(intro_1)                                #  
lines_length_2 = len(intro_2)                                #
line_length = max(lines_length_1, lines_length_2)            #
                                                             #
for x in range(line_length):                                 #
    print('-',end = '')                                      #
print(f'\n{intro_1}')                                        #
print(intro_2)                                               #
print('\nEnter your account number')                         #
for x in range(line_length):                                 #
    print('-', end = '')                                     #
print('\n')                                                  #
#------------------------------------------------------------#

user_account_number = (input('Account Number: '))
with open('/Users/mehulgupta/Documents/Python/bank_records.csv','r') as f:                #opening the file
    file_data = f.readlines()
    result = []
    for x in file_data:
        x = x.replace('\n','')
        result.append(x.split(','))             #here we split all the records into lists individually

    for i,y in enumerate(result):
        if user_account_number in y:            #checking whether the account is valid or not
            a = i
            b = y.index(user_account_number)
            
            check_attempts = 0
            attempts = 2
            while check_attempts < 3:                        #user gets 3 attempts to enter correct atm pin
                user_pin  =input('Enter the atm pin: ')
                if user_pin == result[i][2]:
                    check_attempts = 3
                    print(f'\nWelcome {result[i][1]}!\n')

                    print("1. Withdrawal")
                    print("2. Quick cash")
                    print("3. Balance Inquiry")
                    print("4. Change atm pin")
                    transaction_type = int(input('Enter serial number of transaction you want to perform: '))

                    def withdrawal():
                        amount = 1
                        while amount%100 != 0:
                            amount = int(input('Enter amount to be withdrawn(multiple of 100s) : '))
                            if amount%100 != 0:
                                print('amount is not a multiple of 100, enter a valid amount')
                        
                        print('Withdrawal successful')
                        result[i][4] = int(result[i][4])
                        result[i][4] -= amount
                        print('Available balance = ',result[i][4])
                        result[i][4] = str(result[i][4])
                        
                    def quick_cash():
                        print('1. 1000\n2. 5000\n3. 10000\n4. 20000')
                        result[i][4] = int(result[i][4])
                        option = int(input('Select an option: '))
                        if option == 1:
                            result[i][4] -= 1000
                        elif option == 2:
                            result[i][4] -= 5000
                        elif option == 3:
                            result[i][4] -= 10000
                        elif option == 4:
                            result[i][4] -= 20000
                        else:
                            print('Invalid input')
                        result[i][4] = str(result[i][4])
                        print(f'Available balance = {result[i][4]}')

                    def acc_bal():
                        print(f'Available balance = {result[i][4]}')

                    def atm_pin_change():
                        z = 0
                        attempts_2 = 3
                        while z<3:
                            curr_atm_pin = int(input('Enter your current atm pin : '))
                            global user_pin
                            user_pin = int(user_pin)
                            if curr_atm_pin == user_pin:
                                z = 3
                                new_atm_pin = int(input('Enter your new pin : '))
                                test_verify = 0
                                while test_verify < 3:
                                    new_atm_pin_verify = int(input('Enter new pin again : '))
                                    if new_atm_pin_verify == new_atm_pin:
                                        test_verify = 3
                                        print('New pin set')
                                        result[i][1] = new_atm_pin
                                    else:
                                        print('Wrong pin entered')
                                        test_verify += 1
                            else:
                                print(f'Wrong pin, {attempts_2-1} attempts left')
                                z += 1

                    if transaction_type == 1:
                        withdrawal()

                    if transaction_type == 2:
                        quick_cash()

                    if transaction_type == 3:
                        acc_bal()

                    if transaction_type == 4:
                        atm_pin_change()
                else:
                    print(f'Wrong pin, {attempts} attempts left')
                    check_attempts += 1
                    attempts -= 1
            break
    else:
        print('Invalid account number')

with open('/Users/mehulgupta/Documents/Python/bank_records.csv','w') as f:
    for i in range(len(result)):
        for x in range(len(result[0])):
            if x != len(result[0])-1:
                f.write(f'{result[i][x]},')
            else:
                f.write(f'{result[i][x]}')
        f.write('\n')
    
print('Thank you, please collect your card')
        
#Run whole program untill user exits it