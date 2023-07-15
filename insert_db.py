import mysql.connector as conn
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

host = config['USER']['host']
user = config['USER']['user']
password = config['USER']['password']

# Connection to MySql Server 
mydb = conn.connect(host=host, user=user, password=password) 
cursor = mydb.cursor()

# # Delete all rows 
# cursor.execute("DELETE FROM test_db.test_data")

# # Inserting data into table 
cursor.execute("insert into test_db.test_data values(00, 'Nikhil', 'nikhilshett00@gmail.com',50000000,100)")
cursor.execute("insert into test_db.test_data values(01, 'Guru', 'singhguru9@gmail.com',254000000,100)")
cursor.execute("insert into test_db.test_data values(02, 'Pratik', 'prakkyadac88@gmail.com',23000000,100)")
# # When handling data in database always commit the changes to made  
mydb.commit()

cursor.execute("select * from test_db.test_data")
for i in cursor.fetchall():
    print(i)