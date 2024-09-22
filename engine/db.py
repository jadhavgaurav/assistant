import csv
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

# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/en_in/')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'whatsapp', 'https://web.whatsapp.com')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'chatgpt', 'https://chatgpt.com/')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://youtube.com')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'wingz', 'https://wingz.itvedant.com/index.php/site/login')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'wings', 'https://wingz.itvedant.com/index.php/site/login')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'Hackerrank', 'https://www.hackerrank.com/dashboard')"
# cursor.execute(query)
# con.commit()

## Create contacts Table
## Create a table with the desired columns

cursor.execute('''
               CREATE TABLE IF NOT EXISTS contacts (
                id integer primary key,
                name VARCHAR(200),
                mobile_no VARCHAR(10),
                email VARCHAR(255) NULL)
                ''')


#### 3. Import CSV file into database

## Specify the column indices you want to import (0-based index)
## Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 1]

# ## Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()


# cursor.execute('''DELETE TABLE contacts''')

## To insert contacts manually
# query = "INSERT INTO contacts VALUES (null,'Gaurav Jadhav', '8698027152', null)"
# cursor.execute(query)
# con.commit()

# query = 'aditya karosiya'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])