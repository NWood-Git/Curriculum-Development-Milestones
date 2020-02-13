
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="BAAdmin",
  passwd="password",
  database="BADatabase"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE students (
                      id            INT AUTO_INCREMENT PRIMARY KEY, 
                      name          VARCHAR(255)
                     );""")                
