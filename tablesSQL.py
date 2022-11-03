import sqlite3
from datetime import datetime

conn = sqlite3.connect('db1.sqlite')

cursor = conn.cursor()

#cursor.execute("CREATE TABLE IF NOT EXISTS Students (id int, name Varchar(32), lastname Varchar(32), age int, city Varchar(20))")
#cursor.execute("CREATE TABLE IF NOT EXISTS Courses (id int, name Varchar(32), time_start Varchar(10), time_end Varchar(10))")
#cursor.execute("CREATE TABLE IF NOT EXISTS Student_Courses (student_id int, courses_id int)")

#cursor.executemany("INSERT OR IGNORE INTO Students (id, name, lastname, age, city) VALUES(?, ?, ?, ?, ?)", [(1, 'Max', 'Brooks', 24, 'Spb'),(2, 'John', 'Stones', 15, 'Spb'),(3, 'Andy', 'Wings', 45, 'Manhester'),(4, 'Kate', 'Brooks', 34, 'Spb')])
#cursor.executemany("INSERT OR IGNORE INTO Courses (id, name, time_start, time_end) VALUES(?, ?, ?, ?)", [(1, 'python', '21.07.21','21.08.21'),(2, 'java','13.07.21','16.08.21')])
#cursor.executemany("INSERT OR IGNORE INTO Student_Courses (student_id, courses_id) VALUES(?, ?)", [(1,1),(2,1),(3,1),(4,2)])

#conn.commit()

students_age = cursor.execute("SELECT * FROM Students WHERE age > 30").fetchall()
print(students_age)

students_python = cursor.execute("""SELECT Students.name, Courses.name
	                                FROM Students, Courses, Student_Courses
	                                WHERE (Courses.id = 1) AND (Student_Courses.courses_id = Courses.id) and (Students.id = Student_Courses.student_id)""").fetchall()
print(students_python)

students_python_spb = cursor.execute("""SELECT Students.name, Courses.name
	                                    FROM Students, Courses, Student_Courses
	                                    WHERE  (Courses.id = 1) AND (Student_Courses.courses_id = Courses.id) and (Students.id = Student_Courses.student_id) and (Students.city == 'Spb')""").fetchall()
print(students_python_spb)

conn.commit()
conn.close