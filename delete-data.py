import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="ALLEY08cabby", database="school")
cursor=con.cursor()
pin=int(input("enter pin: "))
query="delete from  school  where pin ={}".format(pin)
cursor.execute(query)
con.commit()
print("deletion successfully.........")