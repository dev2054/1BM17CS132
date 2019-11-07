import sqlite3
connection=sqlite3.connect("studentinfo.db")
connection.execute("CREATE TABLE student_information(ID int primary key not NULL,NAME text  not NULL,AGE int not NULL,ADDRESS varchar(30), CLASS int not NULL);")
print("created")
connection.execute("INSERT INTO student_information(ID,NAME,AGE,ADDRESS,CLASS) VALUES(101, 'MOTE',21,'TABLEA',10)")
connection.execute("INSERT INTO student_information(ID,NAME,AGE,ADDRESS,CLASS) VALUES(102, 'BHAISE',22,'GOTH',8)")
connection.execute("INSERT INTO student_information(ID,NAME,AGE,ADDRESS,CLASS) VALUES(108, 'JALGAIDA',29,'FOHAORPANI',7)")
connection.execute("INSERT INTO student_information(ID,NAME,AGE,ADDRESS,CLASS) VALUES(110, 'HAATI',41,'HATISAR',6)")
connection.commit()
print("info inserted")
disp=connection.execute("SELECT ID,NAME,AGE,ADDRESS,CLASS FROM student_information")
for row in disp:
    print("*"*10)
    print ("ID =", row[0] )
    print ("NAME =", row[1])
    print ("AGE =", row[2] )                   
    print ("ADDRESS =", row[3]) 
    print ("CLASS =", row[4]), "\n"
print( "Operation done successfully")

connection.execute("UPDATE student_information set AGE = 25 where ID = 110") 
connection.commit()
                        
disp=connection.execute("SELECT ID,NAME,AGE,ADDRESS,CLASS FROM student_information")
for row in disp:
    print("*"*10)
    print ("ID =", row[0] )
    print ("NAME =", row[1])
    print ("AGE =", row[2] )                   
    print ("ADDRESS =", row[3]) 
    print ("CLASS =", row[4]), "\n"
print ("update done successfully")




connection.execute("DELETE from student_information where ID = 101;")
                        
connection.commit()

disp=connection.execute("SELECT ID,NAME,AGE,ADDRESS,CLASS FROM student_information")
for row in disp:
    print("*"*10)
    print ("ID =", row[0] )
    print ("NAME =", row[1])
    print ("AGE =", row[2] )                   
    print ("ADDRESS =", row[3]) 
    print ("CLASS =", row[4]), "\n"
print ("delete done successfully");
