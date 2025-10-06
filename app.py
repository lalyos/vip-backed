
import json
import os
import psycopg2
import mysql.connector


# dburl = os.getenv("DB_URL", default="mysql://root:secret@mydb:3306/mysql")

## MARIA
dburl = "mysql://root:secret@172.17.0.8:3306/mysql"
#dburl = "host=172.17.0.8 user=root password=secret dbname=mysql port=3306"

table = os.getenv("DB_TABLE",default= "vip")



## !!!MYSQL!!! code
mydb = mysql.connector.connect(user='root', password='secret',
                              host='172.17.0.8',
                              database='mysql')

# mydb = mysql.connector.connect(dburl)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM vip")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)


## !!!POSTGRES!!! code
# conn = psycopg2.connect(dburl)
# cursor = conn.cursor()
# cursor.execute(f"SELECT * FROM {table}")
# results = cursor.fetchall()
# rows = []
# for row in results:
#     rows.append({'Name': row[0], 'Age': row[1]})
# json_array = json.dumps(rows)

# print(json_array)
