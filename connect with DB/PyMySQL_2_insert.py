import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                     database='python_mysql_class',
                                     user='dba',
                                     password='dbaMySQL80')
my_cursor = connection.cursor()
insert_commit = "INSERT INTO drink VALUES (%s, %s, %s, %s, %s, %s)"
data = ('DR0005', '西瓜汁', None, 'TW', 70, '飲品')
# data = ('DR0006', '西瓜汁', datetime.date(2024, 9, 22), 'TW', 70, '飲品')
my_cursor.execute(insert_commit, data)
connection.commit()
