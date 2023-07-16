import mysql.connector as conn
import configparser

# Data Imported from UCI Repository
# https://archive.ics.uci.edu/dataset/222/bank+marketing

config = configparser.ConfigParser()
config.read("config.ini")

host = config['USER']['host']
user = config['USER']['user']
password = config['USER']['password']

# Connection to MySql Server 
mydb = conn.connect(host=host, user=user, password=password) 
cursor = mydb.cursor()
 
# For Banking Data From UCI in the newly created database 
# db_create = "create database bank_market"
# cursor.execute(db_create)


# Create table this would give an error if the table or database already exists therefore use the 'if not exists' condition when creating tables and database 
# table_create = "create table if not exists bank_market.bank_details(age int, job varchar (30), marital_status varchar(30), education varchar (30), `default` varchar(30), balance int (30) , housing varchar (30), loan varchar (40), contact varchar (30), day int, month varchar (30), duration int, campaign int, pdays int, previous int, poutcome varchar (30), y varchar (30))" 
# cursor.execute(table_create)
# print(cursor.fetchall())

# # Drop Table 
# drop_table = "drop table test_db.bank_details"
# cursor.execute(drop_table)

# To see the tables present in database 
# show tables

# To describe the table 
cursor.execute('describe bank_market.bank_details')   
print(cursor.fetchall())

# mydb.commit()