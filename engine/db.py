import sqlite3

con = sqlite3.connect("victus.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'android studio', 'C:\\Program Files\\Android\\Android Studio1\\bin\\studio64.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/en_in/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'whatsapp', 'https://web.whatsapp.com')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'chatgpt', 'https://chatgpt.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'youtube', 'https://youtube.com')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'wingz', 'https://wingz.itvedant.com/index.php/site/login')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'wings', 'https://wingz.itvedant.com/index.php/site/login')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'Hackerrank', 'https://www.hackerrank.com/dashboard')"
cursor.execute(query)
con.commit()
