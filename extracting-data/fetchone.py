import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="ALLEY08cabby", database="school")
cursor=con.cursor()
query="select * from school"
cursor.execute(query)
data=cursor.fetchone()
print(data)