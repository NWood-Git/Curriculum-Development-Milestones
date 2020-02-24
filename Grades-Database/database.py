
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="BAAdmin",
  passwd="password",
  database="BADatabase"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE student (
                      stud_id       INT AUTO_INCREMENT PRIMARY KEY, 
                      cohort_id     INT NOT NULL,
                      name          VARCHAR(255)
                      FOREIGN KEY (cohort_id)
                        REFERENCES cohort (cohort_id)
                     );""")                

mycursor.execute("""CREATE TABLE cohort (
                      cohort_id     INT AUTO_INCREMENT PRIMARY KEY, 
                      name          VARCHAR(255)
                     );""")                
