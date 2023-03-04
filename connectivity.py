import mysql.connector as c
con=c.connect(host="localhost", user="root", passwd="ALLEY08cabby", database="students")
if con.is_connected():
    print("Successfully Connected....")
else:
    print("Some either happen")
