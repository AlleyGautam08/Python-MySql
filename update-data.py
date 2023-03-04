import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="ALLEY08cabby", database="school")
cursor=con.cursor()
pin=int(input("enter pin: "))
salary=int(input("enter salary: "))
query="update school set salary={} where pin ={}".format(salary,pin)
cursor.execute(query)
con.commit()
print("data update successfully.........")