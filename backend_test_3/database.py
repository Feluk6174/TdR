import mysql.connector

cnx = mysql.connector.connect(user="root", password="Fe1929lix!root", host="127.0.0.1", database="mysql")
cursor = cnx.cursor()
cursor.execute("SELECT * FROM user")
#cursor.execute("SHOW DATABASES")
print(cursor)
for x in cursor:
    print(x)
cnx.close()
