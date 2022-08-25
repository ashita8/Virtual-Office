import ssl  # email
from email.mime.multipart import MIMEMultipart  # email
from email.mime.text import MIMEText

import mysql.connector as connector
import random
import smtplib
import calendar
from win10toast import ToastNotifier
import time

key = 0
k = 0
recieverId = []

class formatedEmail:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='root',
                                     database='vo_virtualOffice1')
        query = "create table if not exists emailgroup (groupName varchar(20) , email varchar(30), Id varchar(20))"
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    def sm(self, to_addr):   #group mail sending
        global sub, body
        print('which type of email you want to send:\n 1: Newsletter \n 2:Transactional\n 3: plain text \n 4: Urrgent '
              'mail \n 5:Milestone\n')
        choice = int(input('enter choice'))
        if choice == 1:
            sub = 'Newletter from virtual office'
            body = 'Hi everyone,\n I wanted to share our policy going forward to make sure we"re all on the same page\n and to keep our team healthy and safe.\n\n 1. You all can feel free to work from home' \
                   '. contact your manager regarding this. \n'+ input('additional information anout staying home') + input("do/don't travel" )+ ' travel'+ 'we donot know yet how it will affect our company' \
                                                                                                                                                       '\n stay safe and healthy \n rest of the information are forwarded by mangers\n' + input('name and position')

        elif choice==2:
            pass
        elif choice ==3:
            sub = 'plain text email from virtual office'
            body = 'Hi everyone, \n I wanted to inform you that'+ input('information')+ '\nplease make sure that '+ input('important alert')+ 'do as directed as soon as possible\n'+input('name position in company')
        elif choice==4:
            sub = 'urrgent mail from virtual office'
            body = 'Hi everyone, \n This is an urrgent message please read carefully\n\n '+ input('enter your text ')+ '\n forward to collegues and start working\n'+input('name and position iin company')
        elif choice==5:
            pass
        else:
            sub = 'no mail'
            body = 'null'
        from_addr = 'virtualoffice456.mypc@gmail.com '

        msg = MIMEMultipart()
        msg['From'] = from_addr
        # to_addr = ''.join(to_add)
        msg['To'] = " ,".join(to_addr)
        msg['subject'] = sub

        msg.attach(MIMEText(body, 'plain'))

        emaila = 'virtualoffice456.mypc@gmail.com'
        password = 'virtualoffice123'

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(emaila, password)
        text = msg.as_string()
        mail.sendmail(from_addr, to_addr, text)
        mail.quit()

    def create_group(self, groupName, member):

        query = "insert into emailgroup1 (groupName,email)values('{}','{}')".format(groupName, member)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("created group: "+ str(groupName))

    def coun(self, ui):
        print(ui)
        query = "SELECT COUNT(groupName) AS groupName FROM emailgroup1 WHERE groupName ='" + ui + "'"
        cur = self.con.cursor()
        cur.execute(query)

        rest = cur.fetchone()
        r = sum(rest)
        return r

    def emailSender(self, ui): #ui contain group name
        p = fe.coun(ui)
        print(p)
        for i in range(0, 1):

            query = " select email from emailgroup1 where groupName = '" + ui + "'"
            cur = self.con.cursor()
            cur.execute(query)
            print(cur)
            res = cur.fetchall()

            if res is not None:
                print(res)
                out = [item for t in res for item in t] #tupple inside list into list

                fe.sm(out)
                print(res)

fe = formatedEmail()   #obj for formated emailclass

    # working programs of the virtual office
def calender():

    choice = input(
        'you want to see whole calender or of a particular month and yer: \n if you want to see for whole year press 1\n if you want to see for a particular month and year press 2 \n for public holidays press any key to progress ')
    if (choice == 1):
        year = int(input('enter the year :'))

        calendar.setfirstweekday(calendar.SUNDAY)

        mycal = calendar.calendar(year)
        print(mycal)
    elif (choice == 2):
        year = int(input('enter the year :'))
        month = int(input('enter month: '))
        calendar.setfirstweekday(calendar.SUNDAY)

        mycal = calendar.month(year, month)
        print(mycal)
    else:
        print(
            "Republic Day	Sun, 26 Jan, 2020\nRama Navami	Thu, 2 Apr, 2020\nGood Friday	Fri, 10 Apr, 2020\nAmbedkar Jayanti	Tue, 14 Apr, 2020\nEid al-Fitr	Mon, 25 May, 2020*\nEid al-Adha	31 Jul – 1 Aug 2020*\nIndian Independence Day	Sat, 15 Aug, 2020\nGandhi Jayanti	Fri, 2 Oct, 2020\nDussehra	Sun, 25 Oct, 2020\nProphets Birthday	28–29 Oct 2020*\nDiwali	Sat, 14 Nov, 2020\nChristmas Day	Fri, 25 Dec, 2020")


def personalNotifier():
    print(
        'DISCRIPTION: \nthis personal notifier sends notification to your syestem to notify you about an \nimportant meeting, timeout, lunch breaks etc. it depends on how you use it')
    tim = input('enter time ')
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == tim:
            print(current_time)
            break
        else:
            pass

    hr = ToastNotifier()
    hr.show_toast("alarm", "this is the message")

# making groups for sending emails
 # the code for switch will always be at the bottom of all its argumented methods


def switch(x):   #for tasks main function
    if x == 1:
        calender()
    elif x == 2:
        personalNotifier()
    elif x == 3:
        groupChoice = int(input('whom you want to send email\n 1:group 2: personal \n'))

        if (groupChoice==1):
            c = int(input('you want to \n 1:create a group 2: send mail to group\n'))
            if c == 1:
                groupName = input('enter group name')
                n = int(input('enter no. of members (should be more than 1)'))

                for i in range(0, n):
                    member = input('enter email of member : ') #email of all the group members
                    fe.create_group(groupName, member)

            elif(c==2):

                ui = input('enter group name')
                fe.emailSender(ui)

            else:
                exit()
        elif(groupChoice==2):   #personal
            from_addr = 'virtualoffice456.mypc@gmail.com '
            to_addr = input('enter email of reciever')
            msg = MIMEMultipart()
            msg['From'] = from_addr
            # to_addr = ''.join(to_add)
            msg['To'] = " ,".join(to_addr)
            msg['subject'] = 'office mail '

            body = input('enter mail body\n (it will sent from the virtual office id )')

            msg.attach(MIMEText(body, 'plain'))

            emaila = 'virtualoffice456.mypc@gmail.com'
            password = ' virtualoffice123'

            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(emaila, password)
            text = msg.as_string()
            mail.sendmail(from_addr, to_addr, text)
            mail.quit()

    elif x==4:
        print('***calculator***\n')
        a = int(input('enter first number'))
        b = int(input('enter second number'))
        c = input('operator')
        if c== '+':
            print('result')
            print(a+b)
        elif c== '-':
            print('result')
            print(a-b)
        elif c== '*':
            print('result')
            print(a*b)
        elif c== '/':
            print('result')
            print(a/b)
        else:
            exit()

    elif(x=='harshit'):
        pass


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='root',
                                     database='vo_virtualOffice1')
        query = 'create table if not exists usertable(userId varchar(50) primary key,userName varchar(200),phone varchar(12),email varchar(40) unique)'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    # insert user deatils into database

    def insert_user(self, userid, username, phone, email):
        query = "insert into usertable (userId,userName,phone,email)values('{}','{}','{}','{}')".format(userid,
                                                                                                        username, phone,
                                                                                                        email)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    # fetching of obtaining data from table
    def fetch_all(self, UserInput):
        query = "select * from usertable where userId = " + UserInput
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("userId : ", row[0])
            print("UserName : ", row[1])
            print("phone : ", row[2])
            print()
            print()
            print()

    def update_user(self, NewuserId, email):  # for updating password
        query = "update usertable set userId ='{}' where email= '{}' ".format(NewuserId, email)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Succesfully updated password')

    def check_userid(self, email,userInput):  # for login

        query = "SELECT * FROM usertable WHERE userId = '{}' and email = '{}'".format(str(userInput),str(email))
        cur = self.con.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if row is not None:
            return 1 #correct password and correct email
        else:
            return 0

    def check_userphone(self, phone, email):  # for forget password

        # send an otp
        query = "select * from usertable where phone = '{}' and email = '{}' " .format(str(phone),str(email))
        cur = self.con.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if row is not None:
            helper.sendemail(email)
        else:
            print('your account does not exist')
            exit()
            return 0

    def sendemail(self, email):
        t = random.randint(10000, 99999)
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        from_addr = 'ashitaaswal8@gmail.com '
        to_addr = [email]
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = " ,".join(to_addr)
        msg['subject'] = 'otp for virtual office'

        body = 'your otp is ' + str(t)

        msg.attach(MIMEText(body, 'plain'))

        emaila = ' ashitaaswal8@gmail.com'
        password = ' ashitaaswal#nina'

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(emaila, password)
        text = msg.as_string()
        mail.sendmail(from_addr, to_addr, text)
        mail.quit()

        for i in range(0, 3):
            otp = int(input('enter the provided otp'))
            if otp == t:
                NewuserId = input('enter new password')
                helper.update_user(NewuserId, email)
                print('done changes')
                exit()
            else:
                print('incorrect otp entered try again! ')


helper = DBHelper()
login = input('you want to login, forget password or register: ')
if (login == 'register' or login == 'REGISTER'):
    username = input('enter your user name : ')
    phone = input('enter phone number Id : ')
    email = input('enter your emailId : ')
    userid = input('enter password') #for password
    print('your user id is', userid)

    helper.insert_user(userid, username, phone, email)
    # helper.check(userid)

elif (login == 'login' or login == 'LOGIN'):
    email = input('enter your email Id')
    userInput = input('enter your password')
    # helper.fetch_all(userInput)
    key = helper.check_userid(email,userInput) #userinpuut have pasword


elif (login == 'forget' or login == 'FORGET'):
    #userName = input('enter your UserName')
    phone = int(input('enter your phone number'))
    email = input('enter your emailId')
    k = helper.check_userphone(phone, email)
    print(k)
if k == -1:
    print('you should register your account firsts')

while True:
    # main started
    if (key == 1):
        print('login succesfull')
        print("enter 1 for: display calender")
        print("enter 2 for: personal notifier")  #task that user can perform
        print('enter 3 for: sending email')
        print('enter 4 for: calculator')
        print('enter 5 for: exit ')

        choice = int(input('enter your choice'))

        switch(choice)
        choice = input('press y to continue')
        if (choice=='y' or choice=='Y'):
            continue


    elif (key==0):
        print('you typed wrong password or email')
    break
