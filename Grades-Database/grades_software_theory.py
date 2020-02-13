
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

mycursor.execute("""CREATE TABLE grades_hello_world (
                      stud_id           INTEGER PRIMARY KEY,
                      arithmetic        INTEGER,
                      name_bindings     INTEGER,
                      operators         INTEGER,
                      python_caches     INTEGER,
                      string_arithmetic INTEGER,
                      user_input        INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (id) 
                     );""")
                     
mycursor.execute("""CREATE TABLE grades_data_types (
                      stud_id           INTEGER PRIMARY KEY,
                      arithmetic        INTEGER,
                      name_bindings     INTEGER,
                      operators         INTEGER,
                      python_caches     INTEGER,
                      string_arithmetic INTEGER,
                      user_input        INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (id) 
                     );""")

mycursor.execute("""CREATE TABLE grades_control_flow (
                      stud_id           INTEGER PRIMARY KEY,
                      arithmetic        INTEGER,
                      name_bindings     INTEGER,
                      operators         INTEGER,
                      python_caches     INTEGER,
                      string_arithmetic INTEGER,
                      user_input        INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (id) 
                     );""")

mycursor.execute("""CREATE TABLE grades_functions (
                      stud_id           INTEGER PRIMARY KEY,
                      arithmetic        INTEGER,
                      name_bindings     INTEGER,
                      operators         INTEGER,
                      python_caches     INTEGER,
                      string_arithmetic INTEGER,
                      user_input        INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (id) 
                     );""")
                     
mycursor.execute("""CREATE TABLE grades_complexity_theory (
                      stud_id           INTEGER PRIMARY KEY,
                      arithmetic        INTEGER,
                      name_bindings     INTEGER,
                      operators         INTEGER,
                      python_caches     INTEGER,
                      string_arithmetic INTEGER,
                      user_input        INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (id) 
                     );""")                     
