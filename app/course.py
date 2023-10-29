from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from datetime import datetime # add the date of college added
from .models import *
#from college_bp import mysql

course_bp = Blueprint('course_bp', __name__)


@course_bp.route('/course')
def course():

    data =  Courses.courseData()
    data1 = Colleges.collegeData()
    cursor.close()

    return render_template('course.html', courses =data, colleges=data1)

@course_bp.route('/insert-course', methods = ['POST'])
def insert_course():
    if request.method == "POST":
        try:
            code = request.form['course_code']
            name = request.form['course_name']
            college_code = request.form['college']

            Courses.addCourse(code, name, college_code)
            flash("Data inserted successfully!", "success")

        except mysql.connector.IntegrityError as e:
            flash("Error: This ID already exists. Please use a unique ID.", "error")        
        return redirect(url_for('course_bp.course'))

@course_bp.route('/update-course', methods=['POST', 'GET'])
def update_course():
    if request.method=='POST':
        # init_id = request.form['id']
        code = request.form['course_code']
        name = request.form['course_name']
        college_code = request.form['college']

        Courses.editCourse(code, name, college_code)

        flash("Data Updated Successfully!")

        return redirect(url_for('course_bp.course'))    
    
@course_bp.route('/delete_course/<string:id>', methods=['POST', 'GET'])
def delete_course(id):
    
    Courses.deleteCourse(id)
    
    flash("Data deleted Successfully!")
    return redirect(url_for('course_bp.course'))