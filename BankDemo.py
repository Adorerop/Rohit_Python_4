class Bank:

    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello ",self.cname,", Your Account Number ",self.acno," Is Opened With ",self.balance," Rs.")

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.balance
            print("Sorry You Need Another ",self.needs," Rs.")

    def checkBalance(self):
        print("Current Balance : ",self.balance)

b1=Bank()

print("*"*50)
cname=input("Enter Customer Name : ")
acno=int(input("Enter Account Number : "))
balance=int(input("Enter Initial Balance : "))
print("*"*50)

b1.openAccount(cname,acno,balance)
print("*"*50)

while True:

    print("*"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)

    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*50)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*50)
    elif choice==3:
        b1.checkBalance()
    else:
        break
    
