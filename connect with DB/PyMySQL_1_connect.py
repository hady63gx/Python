import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                     database='python_mysql_class',
                                     user='dba',
                                     password='dbaMySQL80')
my_cursor = connection.cursor()
my_cursor.execute("SELECT * FROM drink")  # 在這邊就可以選擇需要的就好，以節省記憶體
my_result = my_cursor.fetchall()
print("my_result", my_result)
for x in my_result:
    print(x)
