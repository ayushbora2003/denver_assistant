import sqlite3

con =sqlite3.connect("denver.db")

cursor=con.cursor()
#system_commands:-------
query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

# query="INSERT INTO sys_command VALUES(null,'','')"
# cursor.execute(query)
con.commit()

#web_commands:-----
# query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
# cursor.execute(query)

# query="INSERT INTO web_command VALUES(null,'google','https://www.google.com/')"
# cursor.execute(query)
# con.commit()


#delete :------
# query = "DELETE FROM web_command WHERE name = 'canva' AND url = 'https://www.youtube.com/'"
# cursor.execute(query)
# con.commit()
