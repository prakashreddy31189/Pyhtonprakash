import sqlite3
import os

#data = os.system("sqlite3 mydatabase.db")
#print dir(data)
# create a connection to oyr DB
conn = sqlite3.connect('/home/prakash/Desktop/MyPro/mydatabase.db')
# we have to create a cursor.
cur = conn.cursor()
print dir(conn)
# Place the query and then execute
cur.execute("SELECT * FROM MyApp_person where address='bangalore' OR age>25;")

print cur.fetchall()

cur.close()