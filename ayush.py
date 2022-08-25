import mysql.connector as connector
import datetime
import smtplib
from email.message import EmailMessage
from tabulate import tabulate


class Payroll:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='root', database='vo_virtualOffice1')
        query = 'create table if not exists pay(email varchar(50) ,job varchar(15),BasicSalary int,DA float,HRA float,GrossSalary float,Tax float,NetSalary float,Month varchar(50), Year varchar(10),PAID_UNPAID varchar (10))'
        cur = self.con.cursor()
        cur.execute(query)

    def insert_pay(self, email, job, BasicSalary, DA, HRA, GrossSalary, Tax, NetSalary, Month, Year, PAID_UNPAID):
        query = "insert into pay(email,job,BasicSalary,DA,HRA,GrossSalary,Tax,NetSalary,Month,Year,PAID_UNPAID) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            email, job, BasicSalary, DA, HRA, GrossSalary, Tax, NetSalary, Month, Year, PAID_UNPAID)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def update_pay(self, email, newMonth, newYear, newPAID_UNPAID):
        query = "update pay set Month='{}',Year='{}',PAID_UNPAID='{}'where email='{}'".format(newMonth, newYear,
                                                                                              newPAID_UNPAID, email)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("salery payed to", email)

    def updateall_pay(self, newMonth, newYear, newPAID_UNPAID):
        query = "update pay set Month='{}',Year='{}',PAID_UNPAID='{}'".format(newMonth, newYear, newPAID_UNPAID, )
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def fetch_all(self):
        query = "select * from pay "
        cur = self.con.cursor()
        cur.execute(query)
        print(tabulate(cur,
                       headers=['Email', 'job', 'BasicSalary', 'DA', 'HRA', 'GrossSalary', 'Tax', 'NetSalary', 'Month',
                                'Year', 'PAID_UNPAID'], tablefmt='psql'))

    def delete_pay(self, email):
        query = "delete from pay where email ='{}'".format(email)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    def updaterec_pay(self, email, job, BasicSalary, DA, HRA, GrossSalary, Tax, NetSalary, PAID_UNPAID):
        query = "  update pay set job='{}',BasicSalary='{}',DA='{}',HRA='{}',GrossSalary='{}',Tax='{}',NetSalary='{}',PAID_UNPAID='{}'where email='{}'".format(
            job, BasicSalary, DA, HRA, GrossSalary, Tax, NetSalary, PAID_UNPAID, email)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def fetchone_pay(self, email):

        query = "select * from pay where email = '{}'".format(str(email))
        # print (query)
        cur = self.con.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if row is not None:

            print(row)
        else:
            print('your account does not exist')
            exit()
            return 0


pk = Payroll()
while True:
    print("press 1 to insert new user ")
    print("press 2 to for pay to  individual employee")
    print("press 3 to for pay to all employee ")
    print("press 4 to show status")
    print("press 5 to update Designation of employee")
    print("press 6 to delete   employee  record ")
    print("press 7 to exit")
    print('Enter choice...', end='')
    choice = int(input(""))
    print('*' * 95)

    if choice == 1:
        try:
            email = input("Enter the email of employee")
            job = input("Enter the Designation of employee")
            BasicSalery = int(input("enter the basic Salery"))
            da = float(input('enter  DA rate'))
            hra = float(input('enter HRA rate'))
            tax = float(input('enter Tax rate'))
            DA = BasicSalery * da
            HRA = BasicSalery * hra
            Tax = BasicSalery * tax
            GrossSalery = BasicSalery + DA + HRA
            NetSalary = GrossSalery - tax
            x = datetime.datetime.now()
            Month = x.strftime("%B")
            Year = x.year
            PAID_UNPAID = 'unpaid'
            pk.insert_pay(email, job, BasicSalery, DA, HRA, GrossSalery, Tax, NetSalary, Month, Year, PAID_UNPAID)
        except:
            print("something went wrong")  #inform user abt particular thing

    elif choice == 2:

        username = input("Enter name of employee")
        email = input("enter the email of employee")
        x = datetime.datetime.now()
        Month = x.strftime("%B")
        Year = x.year
        PAID_UNPAID = 'paid'
        pk.update_pay(email, Month, Year, PAID_UNPAID)
        msg = EmailMessage()
        msg.set_content("Hi\n" + str(username) + " your salary is created to your account  for the month of " + str(
            Month) + " \nFor further details contact to your HR.\n\nThank You\nVirtual office team;")
        msg['Subject'] = 'salery created'
        msg['From'] = 'virtualoffice456.mypc@gmail.com '
        msg['To'] = email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('virtualoffice456.mypc@gmail.com', 'virtualoffice123')
        server.send_message(msg)
        server.quit()
        print("email has been send  ")

    elif choice == 3:
        try:
            x = datetime.datetime.now()
            Month = x.strftime("%B")
            Year = x.year
            PAID_UNPAID = 'paid'
            pk.updateall_pay(Month, Year, PAID_UNPAID)
        except Exception as e:
            print("something went wrong", e)



    elif choice == 4:
        v = int(input("Press 1  to Display individual details\nPress 2 Display to all"))
        if v == 1:

            email = input("enter the email of employee")
            pk.fetchone_pay(email)

        elif v == 2:
            pk.fetch_all()
        else:
            print("you enter wrong choice")

    elif choice == 5:
        try:
            email = input("Enter email of employee who is promoted")
            job = input("enter the  new Designation of employee")
            BasicSalery = int(input("enter the basic Salery"))
            da = float(input('enter  DA rate'))
            hra = float(input('enter HRA rate'))
            tax = float(input('enter Tax rate'))
            DA = BasicSalery * da
            HRA = BasicSalery * hra
            Tax = BasicSalery * tax
            GrossSalery = BasicSalery + DA + HRA
            NetSalary = GrossSalery - tax
            PAID_UNPAID = "unpaid"
            pk.updaterec_pay(email, job, BasicSalery, DA, HRA, GrossSalery, Tax, NetSalary, PAID_UNPAID)
        except Exception as e:
            print("something went wrong", e)

    elif choice == 6:
        try:
            email = input("enter email")
            pk.delete_pay(email)
        except Exception as e:
            print("something went wrong", e)

    elif choice == 7:
        break

    else:
        print("you enter the wrong choice ")


