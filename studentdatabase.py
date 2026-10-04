import streamlit as st
import sqlite3
st.title("Student Database")

#connect to database
conn=sqlite3.connect("students.db")

cursor=conn.cursor()

#create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS
students(
id INTEGER PRIMARY KEY
AUTOINCREMENT,
name TEXT,
course TEXT,
year text
)
""")
conn.commit()
#input
st.header("Add Students ")

name=st.text_input("Enter your name: ")
course=st.selectbox("Select course",["CSE","IT",])
year=st.radio("Select your year",["1 st year","2 nd year","3 rd year","4 th year"])

if st.button("Add student"):
    if name=="":
        st.error("Enter the name first")
    else:
        cursor.execute(
         "INSERT INTO students (name,course,year) VALUES (?,?,?)",(name,course,year)
        )
        conn.commit()
        st.success("Student informatin is add successfully")

#Read
if st.button("Show the data of studernts"):
        st.header("All students")
        cursor.execute("SELECT * FROM students")
        students=cursor.fetchall()
        st.dataframe(students)
st.header("Update Students")

student_id=st.number_input("Enter your id to update your data",min_value=1,step=1)
student_course=st.selectbox("Select to update your course",["CSE","IT","CS","AI/ML"])

if st.button("Update your course"):
     if student_id <= 0:
          st.error("Enter the valid id")
     else:
        cursor.execute("UPDATE students SET course=? WHERE id=?",(student_course,student_id))
        conn.commit()
        st.success("Students Updated!")

#Delete
st.header("Delete Student")
delete_id=st.number_input("Enter the id you wanted to delete",min_value=1,step=1)
if st.button("Delete the student from table"):
     cursor.execute("DELETE FROM students WHERE id=?",(delete_id,))
     conn.commit()
     st.success("Student deleted!")

if st.button("Show table"):
     cursor.execute("SELECT * FROM students")
     students=cursor.fetchall()
     st.dataframe(students)

conn.close()     

          


