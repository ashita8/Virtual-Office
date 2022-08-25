#create database first before running the program
# create database vo_virtualOffice1;
# select * from usertable;
# select * from  emailgroup;

# after running the program succesfully run remaining 2 commands

import array
import calendar
import random
import smtplib
import time
from email.mime.multipart import MIMEMultipart  # email
from email.mime.text import MIMEText
from tkinter import *
import datetime
import mysql.connector as connector
from win10toast import ToastNotifier

b=1
key = 0
k = 0
recieverId = [ ]
lst = [ ]

class designation:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='root',
                                     database='vo_virtualOffice1')
        query = "create table if not exists designation (Email_Id varchar(30) , designation varchar(30), protected_password varchar(20))"
        cur = self.con.cursor()
        cur.execute(query)

    def insert_users_for_designation(self, email, designation, key):
        query = "insert into designation (Email_Id,designation,protected_password)values('{}','{}','{}')".format(email,designation,key)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def protected_password(self):
        import random
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
        length = int(input("Enter password length "))
        password = ""
        for i in range(length + 1):
            password += random.choice(chars)
        return(password)

position = designation()

class formatedEmail:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='root',
                                     database='vo_virtualOffice1')
        query = "create table if not exists emailgroup ( groupName varchar(20) , member_email varchar(30), admin_mail varchar(30))"
        cur = self.con.cursor()
        cur.execute(query)


    def sm(self, to_addr):   #group mail sending
        global sub, body
        print('which type of email you want to send:\n 1: Newsletter \n 2:Transactional\n 3: plain text \n 4: Urrgent '
              'mail \n 5:Milestone\n 6:exit\n')
        choice = int(input('enter choice'))
        if choice == 1:
            sub = 'Newletter from virtual office'
            body = 'Hi everyone,\n I wanted to share our policy going forward to make sure we"re all on the same page\n and to keep our team healthy and safe.\n\n 1. You all can feel free to work from home' \
                   '. contact your manager regarding this. \n'+ input('additional information anout staying home') + input("do/don't travel" )+ ' travel'+ 'we donot know yet how it will affect our company' \
                                                                                                                                                       '\n stay safe and healthy \n rest of the information are forwarded by mangers\n' + input('name and position')

        elif choice==2:
            sub= 'this is transactional history mail'
            body = 'you have got money amount of rs mentioned in payroll'
        elif choice ==3:
            sub = 'plain text email from virtual office'
            body = 'Hi everyone, \n I wanted to inform you that'+ input('information')+ '\nplease make sure that '+ input('important alert')+ 'do as directed as soon as possible\n'+input('name position in company')
        elif choice==4:
            sub = 'urrgent mail from virtual office'
            body = 'Hi everyone, \n This is an urrgent message please read carefully\n\n '+ input('enter your text ')+ '\n forward to collegues and start working\n'+input('name and position iin company')
        elif choice==5:
            sub = 'Milestone'
            body = 'Hi \n you have reached a milestone'
        elif choice==6:
            exit()
        else:
            sub = 'no mail'
            body = 'null'
        from_addr = 'virtualoffice456.mypc@gmail.com'

        msg = MIMEMultipart()
        msg['From'] = from_addr

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

    def create_group(self, groupName, member, emailgroup):

        query = "insert into emailgroup(groupName,member_email,admin_mail)values('{}','{}','{}')".format(groupName, member, emailgroup)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("created group: "+ str(groupName))

    def emailSender(self, ui,email): #ui contain group name
        #p = fe.count1(ui)
        #num = int(p)
        for i in range(0, 1):

            query = "SELECT * FROM emailgroup WHERE groupName = '{}' and admin_mail = '{}'".format(str(ui),str(email))
            cur = self.con.cursor()
            cur.execute(query)

            res = cur.fetchall()

            if len(res)==0:
                print('you typed wrong groupname')
                break

            elif res is not None:
                print(res)
                out = [item for t in res for item in t]
                 #tupple inside list into list

                fe.sm(out)

fe = formatedEmail()   #obj for formated emailclass

    # working programs of the virtual office

class Application(Frame):

    def __init__(self,master):

        super (Application,self).__init__(master)
        self.task = ""  #future class subclass which have tasks in future
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets() #.grid() is used to register widgets the grid geometry manager
                            # geometry manager manages the placement and layout of the elements of GUI

    def create_widgets(self):
        self.user_Input = Entry(self, bg="#5BC8AC", bd=29,
                                insertwidth=4, width=24,
                                font=("Verdana", 20, "bold"), textvariable = self.UserIn, justify= RIGHT)
        self.user_Input.grid(columnspan=4)

        self.user_Input.insert(0, "0")
        self.button1 = Button(self, bg="#98DBC6", bd=12,
                              text="1", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(1))
        self.button1.grid(row=2, column=0, sticky=W)

        self.button2 = Button(self, bg="#98DBC6", bd=12,
                              text="2", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(2))
        self.button2.grid(row=2, column=1, sticky=W)

        self.button3 = Button(self, bg="#98DBC6", bd=12,
                              text="3", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(3))
        self.button3.grid(row=2, column=2, sticky=W)

        self.button4 = Button(self, bg="#98DBC6", bd=12,
                              text="4", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)

        self.button5 = Button(self, bg="#98DBC6", bd=12,
                              text="5", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)

        self.button6 = Button(self, bg="#98DBC6", bd=12,
                              text="6", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        self.button7 = Button(self, bg="#98DBC6", bd=12,
                              text="7", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(7))
        self.button7.grid(row=4, column=0, sticky=W)

        self.button8 = Button(self, bg="#98DBC6", bd=12,
                              text="8", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(8))
        self.button8.grid(row=4, column=1, sticky=W)

        self.button9 = Button(self, bg="#98DBC6", bd=12,
                              text="9", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(9))
        self.button9.grid(row=4, column=2, sticky=W)

        self.button0 = Button(self, bg="#98DBC6", bd=12,
                              text="0", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(0))
        self.button0.grid(row=5, column=0, sticky=W)

        self.addition = Button(self, bg="#98DBC6", bd=12,
                               text="+", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                               command=lambda: self.buttonClick("+"))
        self.addition.grid(row=2, column=3, sticky=W)

        self.Subbutton = Button(self, bg="#98DBC6", bd=12,
                                text="-", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                command=lambda: self.buttonClick("-"))
        self.Subbutton.grid(row=3, column=3, sticky=W)

        self.Multbutton = Button(self, bg="#98DBC6", bd=12,
                                 text="*", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                 command=lambda: self.buttonClick("*"))
        self.Multbutton.grid(row=4, column=3, sticky=W)

        self.Divbutton = Button(self, bg="#98DBC6", bd=12,
                                text="/", padx=33, pady=25,
                                command= lambda: self.buttonClick("/"), font=("Helvetica", 20, "bold"))
        self.Divbutton.grid(row=5, column=3, sticky=W)


        self.equalbutton = Button(self, bg="#E6D72A", bd=12,
                                  text="=", padx=100, pady=25,
                                  command = self.CalculateTask, font=("Helvetica", 20, "bold"))

        self.equalbutton.grid(row=5, column=1, sticky=W,columnspan = 2)

        self.clearbutton = Button(self, bg="#E6D72A", bd=12,
                                  text="AC",font=("Helvetica", 20, "bold"),width = 28,padx = 7,command = self.ClearDisplay )

        self.clearbutton.grid(row=1, columnspan=4, sticky=W)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_Input.get()

        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer

        except SyntaxError as e:
            self.displayText("Invald syn")
            self.task = ""

    def displayText(self, value):
        self.user_Input.delete(0, END)
        self.user_Input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_Input.delete(0, END)
        self.user_Input.insert(0, "0")

#app = Application() #object of application class
class Attendance:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='root',
                                     database='vo_virtualOffice1')
        query = "create table if not exists Attendance (SNO varchar(100) , EmailId varchar(30) , starting_date varchar(30), EndingDate varchar(50),No_of_leaves float(2),total_present int(3))"
        cur = self.con.cursor()
        cur.execute(query)

    def insert_user(self,SNO, emailId,starting_date,EndingDate,No_of_leaves,total_present) :
        query="insert into Attendance (SNO ,EmailId,starting_date,EndingDate,No_of_leaves,total_present) values ('{}','{}','{}','{}','{}','{}')".format(SNO,emailId,starting_date, EndingDate,No_of_leaves,total_present)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def update_user(self,EndingDate,total_present,EmailId):
        query = "update Attendance set EndingDate  = '{}' , total_present ='{}' where EmailId='{}' ".format(EndingDate,total_present,EmailId)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def takingAttendance(self):
        global total_present, SNO, datetime
        check = True
        while (check == True):
            #inserting all detais of a use

            login = int(input(
                'press 1 for Attendance\n press 2 if you want to add user\n press 3 for digital clock\n press 4 for exit: '))
            if (login == 1):

                print('\n TAKING ATTENDANCE\n')
                a = int(input('how many are present: '))
                for i in range (0,a):
                    p = input('enter emailId of present ')
                    query= "select total_present from Attendance where emailId = \'{0}\'".format(p)
                    cur = self.con.cursor()
                    cur.execute(query)

                    res = cur.fetchall()
                    out = [item for t in res for item in t]
                    ppp = sum(out)
                    tp = ppp+1
                    print(ppp)
                    present_date1 = str(datetime.datetime.today())  #for todays date time later we alter it
                    present_date2 = present_date1[0:10]

                    #starting_date
                    if res is not None:
                        ad.update_user(present_date2,tp,p)

#[(6,)] is produced when you fetch a value from database

            elif (login == 2):
                # add user
                n = int(input('enter number of records: '))

                for i in range (0,n):
                    import datetime #put above
                    #SNO = i+1
                    emailId = input('\nEnter email of employee: ')
                    starting_date = (input(
                        'Enter starting date (please note that the starting month and ending month must be same i.e current month)(format: yyyy-mm-dd) :  '))
                    EndingDate1 = str (datetime.datetime.today())
                    EndingDate2 = EndingDate1[0:10] # (input(
                        #'enter ending date (please note that the starting month and ending month must be same) (format: yyyy-mm-dd): '))
                    starting = int(starting_date[5:7])
                    ending = int(EndingDate2[5:7])
                    date1 = int(starting_date[8:10])
                    date2 = int(EndingDate2[8:10])
                    #if starting == ending:
                    total_present = (date2 - date1) + 1

                    No_of_leaves = int(input('No of leaves if any till now: '))

                    query = "SELECT COUNT(*) FROM Attendance"
                    cur = self.con.cursor()
                    cur.execute(query)

                    rest = cur.fetchone()
                    total_recd = sum(rest)

                    SNO = total_recd +1

                    ad.insert_user(SNO, emailId, starting_date, EndingDate2, No_of_leaves, total_present)

            if (login == 3):
                #from tkinter import *
                #from tkinter.ttk import *
                from time import strftime

                root = Tk()
                root.title("clock")

                def time():
                    string = strftime("%H:%M:%S:%p")
                    lbl.config(text=string)
                    lbl.after(1000, time)

                lbl = Label(root, font=("calibri", 40, "bold"), background="purple", foreground="white")
                lbl.pack(anchor="center")
                time()
                mainloop()
            elif (login==4):
                check = False

ad = Attendance()

def calender():
    checking = 1
    while checking == True:
        c = int(input(
            'you want to see whole calender or of a particular month and yer: \n\nif you want to see for whole year press 1\n if you want to see for a particular month and year press 2 \n press 3 for exit calender \n for public holidays press any key to progress '))
        if c == 1:

            year = int(input('enter the year :'))
            calendar.setfirstweekday(calendar.SUNDAY)

            mycal = calendar.calendar(year)
            print(mycal)
        elif c == 2:
            year = int(input('enter the year :'))
            month = int(input('enter month: '))
            calendar.setfirstweekday(calendar.SUNDAY)

            mycal = calendar.month(year, month)
            print(mycal)
        elif c == 3:
            checking = False

        else:

            print(
                "Republic Day	Sun, 26 Jan, 2020\nRama Navami	Thu, 2 Apr, 2020\nGood Friday	Fri, 10 Apr, 2020\nAmbedkar Jayanti	Tue, 14 Apr, 2020\nEid al-Fitr	Mon, 25 May, 2020*\nEid al-Adha	31 Jul – 1 Aug 2020*\nIndian Independence Day	Sat, 15 Aug, 2020\nGandhi Jayanti	Fri, 2 Oct, 2020\nDussehra	Sun, 25 Oct, 2020\nProphets Birthday	28–29 Oct 2020*\nDiwali	Sat, 14 Nov, 2020\nChristmas Day	Fri, 25 Dec, 2020")


def personalNotifier():
    print(
        'DISCRIPTION: \nthis personal notifier sends notification to your syestem to notify you about an \nimportant meeting, timeout, lunch breaks etc. it depends on how you use it')
    print('input time in format of 24 hour clock. i.e hh:mm:ss')
    tim = input('enter time ')
    message = input('enter message ')
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == tim:
            print(current_time)
            break
        else:
            pass

    hr = ToastNotifier()
    hr.show_toast("alarm", message)

# making groups for sending emails
 # the code for switch will always be at the bottom of all its argumented methods





def switchFun(x,email):   #for tasks main function
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
                    fe.create_group(groupName, member,email)

            elif(c==2):

                ui = input('enter group name')
                fe.emailSender(ui,email)

            else:
                exit()
        elif(groupChoice==2):   #personal
            from_addr = 'virtualoffice456.mypc@gmail.com '
            to_addr = input('enter email of reciever')
            msg = MIMEMultipart()
            msg['From'] = from_addr

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

        calculator = Tk()
        calculator.title("Calculator")
        app = Application(calculator)
        calculator.resizable(width=False, height=False)

        calculator.mainloop()

    elif x ==5:
        ad.takingAttendance()





    elif x ==6:
        exit()

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='root',
                                     database='vo_virtualOffice1')
        query = 'create table if not exists usertable(userId varchar(50) primary key,userName varchar(200),phone varchar(12),email varchar(40) unique)'
        cur = self.con.cursor()
        cur.execute(query)
        #print("Created")

    # insert user deatils into database

    def insert_user(self, userid, username, phone, email):
        query = "insert into usertable (userId,userName,phone,email)values('{}','{}','{}','{}')".format(userid,
                                                                                                        username, phone,
                                                                                                        email)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        #print("user saved to db")

    # fetching of obtaining data from table
    def fetch_all(self, UserInput):
        query = "select * from usertable where userId = " + UserInput
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("userId : ", row[0])
            print("UserName : ", row[1])
            print("phone : ", row[2])

    def update_user(self, NewuserId, email):  # for updating password
        query = "update usertable set userId ='{}' where email= '{}' ".format(NewuserId, email)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Succesfully updated password\n')

    def check_userid(self, email,userInput):  # for login

        query = "SELECT * FROM usertable WHERE userId = '{}' and email = '{}'".format(str(userInput),str(email))
        cur = self.con.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if row is not None:
            return 1  #correct password and correct email
        else:
            return 0
    def check_for_register(self,email):
        query = "SELECT * FROM usertable WHERE email = '{}'".format(str(email))
        cur = self.con.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if row is not None:
            return 1  # correct email
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

        from_addr = 'virtualoffice456.mypc@gmail.com '
        to_addr = [email]
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = " ,".join(to_addr)
        msg['subject'] = 'otp for virtual office'

        body = 'your otp is ' + str(t)

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
#while loop for options
check = True

while (check == True):
    try:
        login = int(input('press 1 for register\n press 2 for login\n press 3 if you forget password\n press 4 for exit: '))

        if (login == 1):
            username = input('enter your user name : ')
            phone = input('enter phone number Id : ')
            email = input('enter your emailId : ')
            userid = input('enter password: ')
            designation = input('enter your designation: ')                                    #for password
            #print('your user id is', userid)

            res = helper.check_for_register(email)
            if res==1:
                print('Create with another email this account already exists \n')
            else:
                print('registered sucessfully\n')

            helper.insert_user(userid, username, phone, email)




            if designation == 'HR' or designation== 'hr':
                protected_password = position.protected_password()
                print('As you are at designation HR: \n' + protected_password + ' this is a protected password that will give you acces to attendance and payroll system.')
                position.insert_users_for_designation(email,designation,protected_password)
            else:
                position.insert_users_for_designation(designation,email,'notvalid')

        elif (login ==2):
            email = input('enter your email Id')
            userInput = input('enter your password')

            key = helper.check_userid(email,userInput)  #userinpuut have pasword

            while (b == True):
                # main started
                if (key == 1):
                    #print('login succesfull ')
                    print("enter 1 for: display calender ")
                    print("enter 2 for: personal notifier ")  #task that user can perform
                    print('enter 3 for: sending email ')
                    print('enter 4 for: calculator ')
                    print('enter 5 for: Attendance ')
                    print('enter 6 for: to close this application \n')

                    choice = int(input('enter your choice '))
                    if (choice== 6):
                        b = False
                         # if email is same as login email

                    switchFun(choice, email)

                else:
                    print('you typed wrong password or email\n')
                    break


        elif (login ==3):

            phone = int(input('enter your phone number'))
            email = input('enter your emailId')
            k = helper.check_userphone(phone, email)

        if k == -1:
            print('you should register your account firsts\n')

        elif(login == 4):
            check = False

    except ValueError as e:
        print('\nenter a number not character or floating number')
