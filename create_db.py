import mysql.connector as conn
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

host = config['USER']['host']
user = config['USER']['user']
password = config['USER']['password']

# Connection to MySql Server 
mydb = conn.connect(host=host, user=user, password=password) 
mydb.database = 'test_db'
# Use Cursor to Execute Queries 
cursor = mydb.cursor()

# To Create Database 
cursor.execute("create database test_db")

# Show All the Database available in the local server
cursor.execute("show databases")

# Create a table inside a database 
query = "create table test_db.test_data(emp_id int (10), emp_name varchar (80), emp_email varchar(80))"
cursor.execute(query)

table = "select * from test_db.test_data"
table_db = cursor.execute(table)
print(table_db)

# Inserting new columns 
new_table = "alter table test_db.test_data add column salary int (40), add column attendence varchar (8)"
cursor.execute(new_table)

mydb.commit()



