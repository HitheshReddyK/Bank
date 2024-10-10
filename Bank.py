import random

class Bank:

    def create_account(self):

        self.name=input('\t\tEnter your name: ')

        self.contact_number=int(input('\t\tEnter Contact Number: '))

        self.account_balance=0

        self.account_type=input("\t\tAccount Types: \n\t\t1.Savings Account \n\t\t2.Current Account \n\t\t3.Business Account \nEnter Account Type: ")

        self.account_number=int(random.random()*100)

        self.withd=0

        self.dep=0

        print('\n')

        print('Your Account Number is: ',self.account_number)

    def print_details(self):

        print('\n')

        print('Your Account Details: ')

        print('\tAccount Number: ',self.account_number)

        print('\tAccount Holder Name: ',self.name)

        print('\tAccout Type: ',self.account_type)

        print('\tYour Account Balance:',self.account_balance)

        print('\tContact Number: ',self.contact_number)

    def deposite(self):

        print('\n')

        print('Deposit Successfull..')

        print('\tAvailable Balance is: ',self.account_balance)

    def withdraw(self):

        print('\n')

        print('Withdraw Successfull..')

        print('\tAvailable Balance is: ',self.account_balance)

    def statement(self):

        print('\n')

        print('Your Trasaction Amout:')

        print('\tTotal Deposite: ',self.dep)

        print('\tTotal Withdrwal: ',self.withd)

        print('\tTotal Available Balance: ',self.account_balance)

 

bank_details={}

       

while True:

    print('\n')

    print('How Can I Help You:')

    print('\t\t1.Create Account')

    print('\t\t2.View Account Details By Account Number')

    print('\t\t3.Deposit')

    print('\t\t4.Withdraw')

    print('\t\t5.Fund Transfer')

    print('\t\t6.Statement')

    print('\t\t7.Exit')

    choice=int(input('Enter your Choice: '))

   

    if choice==1:

        b=Bank()

        b.create_account()

        bank_details[b.account_number]=b

    elif choice==2:

        no=int(input('\t\tEnter your Account Number: '))

        if no not in bank_details:

            print('Account is Not Present in our Bank. Please,Enter Valid Account Number..')

        else:

            temp=bank_details[no]

            temp.print_details()

    elif choice==3:

        no=int(input('\t\tEnter your Account Number: '))

        if no not in bank_details:

            print('Account is Not Present in our Bank. Please,Enter Valid Account Number..')

        else:

            temp=bank_details[no]

            amount=int(input('\t\tEnter the Amount to Deposit: '))

            temp.account_balance += amount

            temp.dep += 1

            temp.deposite()

    elif choice==4:

        no=int(input('\t\tEnter your Account Number: '))

        if no not in bank_details:

            print('Account is Not Present in our Bank. Please,Enter Valid Account Number..')

        else:

            temp=bank_details[no]

            amount=int(input('\t\tEnter the Amount to Withdraw: '))

            if temp.account_balance>=amount:

                temp.account_balance -= amount

                temp.withd += 1

                temp.withdraw()

                print('Transaction Successfull..')

            else:

                print('"In-sufficient Funds.."')

    elif choice==5:

        no=int(input('\t\tEnter your Account Number of Sender: '))

        no1=int(input('\t\tEnter your Account Number of Reciever: '))

        if no and no1 not in bank_details:

            if no not in bank_details:

                print("Sender's Account is Not Present in our Bank. Please,Enter Valid Account Number..")

            else:

                print("Reciever's Account is Not Present in our Bank. Please,Enter Valid Account Number..")

        else:

            temp=bank_details[no]

            temp1=bank_details[no1]

            amount=int(input('\t\tEnter the Amount to send: '))

            if temp.account_balance >= amount:

                temp.account_balance -= amount

                temp.withd += 1

                temp1.account_balance += amount

                temp1.dep +=1

            else:

                print('"In-sufficient Funds.."')

            temp.print_details()

            temp1.print_details()

    elif choice==6:

        no=int(input('\t\tEnter your Account Number: '))

        if no not in bank_details:

            print('Account is Not Present in our Bank. Please,Enter Valid Account Number..')

        else:

            temp=bank_details[no]

            temp.statement()

    elif choice==7:

        break

