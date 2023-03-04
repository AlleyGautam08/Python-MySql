import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="ALLEY08cabby", database="school")
cursor=con.cursor()
while True:
    pin= int(input("enter your pin: "))
    teacherName=input("enter teacher name: ")
    salary=int(input("enter salary:"))
    subject=input("enter subject: ")
    query="insert into school values({},'{}',{},'{}')".format(pin,teacherName, salary,subject)
    cursor.execute(query)
    con.commit()
    print("data inserted sucessfully")

