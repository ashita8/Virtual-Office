'''from textblob import TextBlob

file1 = open("txt","r+")
a= file1.read()
print("original text : "+str(a))

b= TextBlob(a)
print("corrected text : "+str(b.correct()))
#this correct automaticlly correct all the spelling
file1.close()
d=open("1.txt","w")
d.write(str(b.correct()))
d.close()'''


# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
'''class Bank_Account:

    def __init__(self, name, bno):
        self.balance = 0
        self.name = 'name'
        self.bno = 0
        print("Hello!!! Welcome to Bank")

    def deposit(self):

        print(self.name)
        print(self.bno)
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)


s = []

s.append(Bank_Account('Akash', 2))
s.append(Bank_Account('Deependra', 40))
s.append(Bank_Account('Reaper', 44))

# s = Bank_Account()

# Calling functions with that class object
for obj in s:

    c = int(input('enter your choice 1: deposit 2: withdraw 3: display'))
    if c == 1:

        obj.deposit()
    elif c == 2:

        obj.withdraw()
    else:
        obj.display()'''

import datetime
import smtplib
from prettytable import PrettyTable

username = input("enter user name ")
email = input("enter user email id ")
phno = input("enter mobile number")
Designation = input("Designation:")
days = float(input('enter the total working days: '))
wages = int(input("enter the wages per day :"))
basic = days*wages
Housing = basic * 0.095
Transport = basic * 0.076
Tax = basic*0.03
ctc = basic*0.05
Net_salery = basic+Housing+Transport-Tax-ctc
mydate = datetime.datetime.now()
mydate.strftime("%B")
t = PrettyTable(['Name','Basic','ctc','T.Tax','Transport','Housing','Month','Net_salery'])
t.add_row([username,basic,ctc,Tax,Transport,Housing,(mydate.strftime("%B")),Net_salery])
print(t)
sender_mail = "virtualoffice456.mypc@gmail.com"
rec_mail = email
password = input("plz enter the password")
message = "Hi\t"+str(username)+"\n\nyour salery "+str(Net_salery)+"is created to your account VO904 for the month of" +str(mydate.strftime("%B"))+" \nfor further details contact to your manager:8279980122.\n\nThank You\nVitual office team;"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_mail,password)
print('login suceesfully')
server.sendmail(sender_mail,rec_mail,message)
print("email has been to",rec_mail)
