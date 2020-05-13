import mysql.connector

con=mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cur=con.cursor()

word=input("enter a word: ")

q=cur.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s' " % word )
r=cur.fetchall()
for i in r:
    print(i[0])