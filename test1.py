import mysql.connector as conn
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

password = config['USER']['password']

# Connection to MySql Server 
mydb = conn.connect(host="localhost", user="root", password=password) 

print(mydb)