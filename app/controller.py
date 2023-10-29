from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from datetime import datetime # add the date of student added
from .models import *
#from student_bp import mysql

student_bp = Blueprint('student_bp', __name__)


# student_bp.secret_key = 'shhh'

# student_bp.config['MYSQL_HOST'] = 'localhost'
# student_bp.config['MYSQL_USER'] = 'root'
# student_bp.config['MYSQL_PASSWORD'] = '1234'
# student_bp.config['MYSQL_DB'] = 'ssis_web'

# mysql_conn = mysql.connector.connect( 
#     host=student_bp.config['MYSQL_HOST'],
#     user=student_bp.config['MYSQL_USER'],
#     password=student_bp.config['MYSQL_PASSWORD'],
#     database=student_bp.config['MYSQL_DB']
# )

# cursor = mysql_conn.cursor(student_bp)

@student_bp.route('/')
def Index():
    data = Students.studentData()
    data1 = Courses.courseData()

    return render_template('student.html', students =data, courses = data1)

@student_bp.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        try:
            id = request.form['idnum']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            course = request.form['course']
            year = request.form['year']
            gender = request.form['gender']

            Students.addStudent(id, firstname, lastname, course, year, gender,)
            flash("Data inserted successfully!", "success")
        except mysql.connector.IntegrityError as e:
            flash("Error: This ID already exists. Please use a unique ID.", "error")
        return redirect(url_for('student_bp.Index'))

@student_bp.route('/update', methods=['POST', 'GET'])
def update():
    if request.method=='POST':
        # init_id = request.form['id']
        id = request.form['idnum']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        course = request.form['course']
        year = request.form['year']
        gender = request.form['gender']
        
        Students.editStudent(id, firstname, lastname, course, year, gender)
        flash("Data Updated Successfully!")
        return redirect(url_for('student_bp.Index'))

@student_bp.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete(id):
    Students.deleteStudent(id)
    flash("Data deleted Successfully!")
    return redirect(url_for('student_bp.Index'))

@student_bp.route('/search/<string:id>', methods=['POST', 'GET'])
def search(id):
    if request.method=='POST':
        id = request.form['search']
        data =  Students.searchStudent(id)        
    
    return render_template('student.html', result =data)

