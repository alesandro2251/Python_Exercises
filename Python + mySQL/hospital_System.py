# In this exercise, We are implementing the Hospital Information System. In this exercise,
# I have created two tables, Hospital and Doctor. You need to create those two tables on your
# database server before starting the exercise.


import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='#',
    password='#',
    database='HospitalSystem'
)

mycursor = db.cursor()

# Creating Hospital Table
mycursor.execute(
    "CREATE TABLE Hospital (Hospital_ID int PRIMARY KEY AUTO_INCREMENT, Hospital_Name varchar(60) NOT NULL , BED_COUNT int NOT NULL )")

# Filling Hospital Table
query = "INSERT INTO Hospital (Hospital_Name, BED_COUNT) VALUES (%s, %s)"
value1 = ['Mayo Clinic', 200]
value2 = ['Cleveland Clinic', 400]
value3 = ['Johns Hopkins', 1000]
value4 = ['UCLA Medical Center', 200]
mycursor.execute(query, value2)
mycursor.execute(query, value3)
mycursor.execute(query, value4)
db.commit()

# Creating Doctor Table
mycursor.execute(
    "CREATE TABLE Doctor( Doctor_Id INT UNSIGNED NOT NULL, Doctor_Name TEXT NOT NULL, Hospital_Id INT NOT NULL, Joining_Date DATE NOT NULL, Speciality TEXT NULL, Salary INT NULL, Experience INT NULL, PRIMARY KEY (Doctor_Id))")
# Filling Doctor Table
mycursor.execute(
    "INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) VALUES ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL)")
db.commit()
