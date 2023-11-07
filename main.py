import mysql.connector
class library_mgm:

    def __init__(self):
        self.options()

    def options(self):

        print("""
            press 1 to create your member Id: 
            press 2 to show authors: 
            press 3 to show genres:
            press 4 to show books:
            press 5 to borrow book:
            press 6 to continue or exit:
            """)
        opt = int(input("Enter your choice: "))
        if opt == 1:
            MemberId=input("Enter your preferred id: ")
            FirstName=input("Enter your First Name: ")
            LastName=input("Enter your last Name: ")
            Email=input("Enter your email id: ")
            Phone=input("Enter your phone number: ")

            try:
                insert="insert into Members (MemberId,FirstName,LastName,Email,Phone) values(%s,%s,%s,%s,%s)"
                val=(MemberId,FirstName,LastName,Email,Phone)
                mycursor.execute(insert,val)
                mydb.commit()
                print(mycursor.rowcount,"Data inserted successfully.. (;")
            except:
                print("Something went wrong...:(")

            library_mgm()

        elif opt == 2:
            try:
                show="select * from authors"
                mycursor.execute(show)
                myresult=mycursor.fetchall()
                for x in myresult:
                    print(x)
            except:
                print("something went wrong..):")

            library_mgm()
        elif opt == 3:
            try:
                show="select * from genres"
                mycursor.execute(show)
                myresult=mycursor.fetchall()
                for x in myresult:
                    print(x)
            except:
                print("something went wrong..):")

            library_mgm()
        elif opt == 4:
            try:
                show="select * from books"
                mycursor.execute(show)
                myresult=mycursor.fetchall()
                for x in myresult:
                    print(x)
            except:
                print("something went wrong..):")

            library_mgm()
        elif opt == 5:
            id=tuple(input("Enter book id to borrow book: "))
            alter="select title from books where BookId=%s"
            val=(id)
            mycursor.execute(alter,val)
            myresult=mycursor.fetchall()
            for x in myresult:
                print("you are borrowing a book called ",x)
            temp=True
            while temp:
                LoanId=input("Create your LoanId and Remember it: ")
                MemberId=input("Enter your MemberId: ")
                BookId=input("Enter BookId you want to borrow: ")
                DateBorrowed=input("Enter Date to be borrow in yy-mm-dd: ")
                DueDate=input("Enter Due Date in yy-mm-dd: ")
                alter="insert into loans(LoanId,MemberId,BookId,DateBorrowed,DueDate) values(%s,%s,%s,%s,%s)"
                val=(LoanId,MemberId,BookId,DateBorrowed,DueDate)
                mycursor.execute(alter,val)
                mydb.commit()
                print(mycursor.rowcount,"You have borrowed the book")
                temp=False
            temp2=True
            while temp2:
                alter="UPDATE Books SET CopiesAvailable = CopiesAvailable - 1 WHERE BookID =%s"
                val=(id)
                mycursor.execute(alter,val)
                mydb.commit()
                print(mycursor.rowcount,"Congrats")
                temp2=False

            library_mgm()
        elif opt == 6:
            user = input("press Y for continue Q for quit")
            if user == 'Y' or user == 'y':
                self.option()
            else:
                print("bye... see you again")

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='@123456',
    database='library_mgm'
)

mycursor=mydb.cursor()
obj1 = library_mgm()
