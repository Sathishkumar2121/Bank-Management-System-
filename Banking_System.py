import pickle
import os
import pathlib

class Accounts:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccounts(self):
        self.accNo= int(input("Enter thr account no : "))
        self.name= input("Enter the account holder name : ")
        self.type= input("Enter the type of account [C/S] : ")
        self.deposit= int(input("Enter The Initial amount(>= 500 for Saving and >=1000 for current : "))
        print("\n\n\nAccount Created")

    def showAccounts(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ",self.name)
        print("Type of Account :",self.type)
        print("Balance : ",self.deposit)

    def modifyAccounts(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name : ")
        self.deposit = int(input("Modify Balance : "))

    def depositAmounts(self,amount):
        self.deposit += amount

    def withdrawAmounts(self,amount):
        self.deposit -= amount
   
    def report(self):
        print(self.accNo, " ",self.name, " ",self.type, " ",self.deposit)

    def getAccountsNo(self):
        return self.accNo

    def getAccountsHolderName(self):
        return self.name

    def getAccountsType(self):
        return self.type

    def getDeposit(self):
        return self.deposit

def intro():
    print("\t\t\t\t*******************************************")
    print("\t\t\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t*******************************************")
    print("\t\t\t\tBrought To You By - Prasun Roy")
    print("\t\t\t\tPress enter for main menu")
    input()

def writeAccounts():
    account = Accounts()
    account.createAccounts()
    writeAccountsFile(account)

def displayAll():
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data','rb')
            mylists =pickle.load(infile)
            for items in mylists :
                print(items.accNo," ",items.name," ",items.type," ",items.deposit )
            infile.close()

        else:
            print("No records to display")

def displayssp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for items in mylist:
            if items.accNo == num:
                print("Your Account Balance is = ",items.deposit)
                found = True
    else:
        print("No records to search")
    if not found:
        print("No existing record with this number")

def depositAndWithdraw(num1,num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data","rb")
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for items in mylist:
            if items.accNo == num1 :
                if num2 == 1:
                    amount = int(input("Enter the amount of deposit : "))
                    items.deposit += amount
                    print("Your account is updated")

                elif num2 == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= items.deposit:
                        items.deposit -= amount
                    else :
                        print("You cannot withdraw larger amount")

    else:
        print("No records to Search")

    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist,outfile)
    outfile.close()
    os.rename('newaccounts.data','accounts.data')
