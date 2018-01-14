import random
import sys
import base64

class Bank:


    def intro():
        star = '*'*37
        print(star)
        print('\n')
        print('\t WELCOME TO BMS')
        print('\t Bank Managemetn System')
        print('\n')
        print(star)
        print('\n')
        print('Developed By Avishek Chaudhary')
        print('Press Enter for Menu...')
        input('')
        bank.Main()

    # def AlreadyAccount():
    #     while True:
    #         yn = input("Press (Y or y) to Enter or (N or n) to Create New Account: ")

    #         if yn == 'Y' or yn == 'y' :
    #             account = input('Enter Account Number: ')
    #             with open('newacc.txt','r') as f:
    #                 line = f.readline()
    #                 if account in line:
    #                     bank.Display_All()
    #             break
    #         elif yn == 'N' or yn == 'n':
    #             bank.CreateAccount()

    #         else:
    #             print("Invalid Choice!!\nPlease Enter Valid Option.")


    def CreateAccount():
        account = random.randint(100,10000)
        name = input('Name: ')
        address = input('Address: ')
        amount = int(input('Amount: '))

        with open('newacc.txt','w') as newaccount:
            newaccount.write('Account: '+str(account))
            newaccount.write('\n')
            newaccount.write('Name: '+name)
            newaccount.write('\n')
            newaccount.write('Address: '+address)
            newaccount.write('\n')
            newaccount.write('Amount: %d' % (amount))
            newaccount.write('\n')
            newaccount.close()
        bank.Main()

    def Exit():
        print('Thank you visit again....')
        sys.exit()


    def NewPassword():
        pwd = input('Create New Password: ')
        repwd = input('Re-Enter New Password: ')
        with open('password.txt','wb') as cpwd:
            
            if pwd == repwd:
                b = bytes(pwd, 'utf-8')
                c = base64.b64encode(b)
                cpwd.write(c)
                print('New password set successfully..')
                print('Please Re-Login')
            else:
                print('Password Doesn\'t Match..' )
                bank.NewPassword()
            cpwd.close()


    def oldPassword():
        try:
            with open('password.txt','rb') as oldpass:
                p = oldpass.read()
                temp = base64.decodebytes(p).decode('utf-8','ignore')
                #print(temp)
                password = input('Enter Your Password: ')
                if password == temp:
                    bank.intro()
                else:
                    print('Wrong password..')
        except IOError:
            bank.NewPassword()

    def changePassword():
        try:
            with open('password.txt','rb') as passw:
                p = passw.read()
                temp = base64.decodebytes(p).decode('utf-8','ignore')
                #print(temp)
                passw.close()
                pwd = input('Enter Current Password: ')
                if pwd == temp:
                    bank.NewPassword()
                else:
                    print('Current Password is Incorrect..')
                    print('Logged Out..')
        except IOError:
            print('file error...')

    def WithdrawAmount():
        dicto = {}
        with open('newacc.txt','r') as newaccount:
            for line in newaccount:
                k, v = line.split()
                dicto[k] = v
            print('Total Amount: '+dicto['Amount:'])
            newaccount.close()
        newamount = int(input('Enter withdraw Amount: '))
        with open('newacc.txt','w') as newaccount:
            dicto['Account:'] = newaccount.write('Account: '+dicto['Account:'])
            newaccount.write('\n')
            dicto['Name:'] = newaccount.write('Name: '+dicto['Name:'])
            newaccount.write('\n')
            dicto['Address:'] = newaccount.write('Address: '+dicto['Address:'])
            newaccount.write('\n')
            dicto['Amount:'] = int(dicto['Amount:'])
            dicto['Amount:'] -= newamount
            dicto['Amount:'] = newaccount.write('Amount: '+str(dicto['Amount:']))
            newaccount.close()
        with open('newacc.txt','r') as newaccount:
            for line in newaccount:
                k, v = line.split()
                dicto[k] = v
            print('New Amount is: '+dicto['Amount:'])
            newaccount.close()

    def DepositAmount():
        dicto = {}
        with open('newacc.txt','r') as newaccount:
            for line in newaccount:
                k, v = line.split()
                dicto[k] = v
            print('Old Amount: '+dicto['Amount:'])
            newaccount.close()
        newamount = int(input('Enter New Amount: '))
        with open('newacc.txt','w') as newaccount:
            dicto['Account:'] = newaccount.write('Account: '+dicto['Account:'])
            newaccount.write('\n')
            dicto['Name:'] = newaccount.write('Name: '+dicto['Name:'])
            newaccount.write('\n')
            dicto['Address:'] = newaccount.write('Address: '+dicto['Address:'])
            newaccount.write('\n')
            dicto['Amount:'] = int(dicto['Amount:'])
            dicto['Amount:'] += newamount
            dicto['Amount:'] = newaccount.write('Amount: '+str(dicto['Amount:']))
            newaccount.close()
        with open('newacc.txt','r') as newaccount:
            for line in newaccount:
                k, v = line.split()
                dicto[k] = v
            print('New Amount is: '+dicto['Amount:'])
            newaccount.close()

    def BalanceEnquiry():
        dicto = {}
        while True:
            accountno = int(input('Enter your Account Number: '))
            with open('newacc.txt','r') as newaccount:
                for line in newaccount:
                    k,v = line.split()
                    dicto[k] = v
                if accountno == int(dicto['Account:']):
                    print('Your Total Balance is: '+dicto['Amount:'])
                    print('Thank You!')
                    break
                else:
                    print('Wrong Account Number Please Enter Again!')
                newaccount.close()

    def Display_All():
        dicto = {}
        with open('newacc.txt','r') as newaccount:
            for line in newaccount:
                k, v = line.split()
                dicto[k] = v
                print(k,v)
            newaccount.close()
        bank.Main()


    def Main():
        while True:
            print("*"*17+"MAIN MENU"+"*"*17)
            print("\t1. CREATE ACCOUNT")
            print("\t2. Display Account info")
            print("\t3. CHANGE PASSWORD")
            print("\t4. WITHDRAW AMOUNT")
            print("\t5. DEPOSIT AMOUNT")
            print("\t6. BALANCE ENQUIRY")
            #print("\t7. ALREADY ACCOUNT")
            print("\t7. Exit")
            print("\tENTER YOUR CHOICE FROM (1-7)")
            print("*"*43)
            print("\n")
            dicto = {}
            with open('newacc.txt','r') as newaccount:
                for line in newaccount:
                    k, v = line.split()
                    dicto[k] = v
                name = dicto['Name:']
                print('Welcome User '+name)
                print('\n')
                newaccount.close()

            choice = int(input("Enter your Choice: "))

            if choice == 1:
                bank.CreateAccount()
                break

            elif choice == 2:
                bank.Display_All()
                break

            elif choice == 3:
                bank.changePassword()
                break

            elif choice == 4:
                bank.WithdrawAmount()
                break

            elif choice == 5:
                bank.DepositAmount()
                break

            elif choice == 6:
                bank.BalanceEnquiry()
                break

            # elif choice == 7:
            #     bank.AlreadyAccount()
            #     break

            elif choice == 7:
                bank.Exit()
                break

            else:
                print("+"*59)
                print("\n\tWrong Choice!!\n")
                print("\tPlease Choose Correct Option.\n")
                print("+"*59)


bank = Bank
#bank.Display_All()
bank.oldPassword()
#bank.validate_account()
