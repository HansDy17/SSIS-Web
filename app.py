from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime # add the date of student added
import models

app = Flask(__name__)

app.secret_key = 'shhh'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'ssis_web'

mysql_conn = mysql.connector.connect( 
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

cursor = mysql_conn.cursor(app)

@app.route('/')
def Index():

    data = models.Students.studentData()

    data1 = models.Courses.courseData()

    return render_template('index.html', students =data, courses = data1)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        try:
            id = request.form['idnum']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            course = request.form['course']
            year = request.form['year']
            gender = request.form['gender']

            models.Students.addStudent(id, firstname, lastname, course, year, gender)
            flash("Data inserted successfully!", "success")
        except mysql.connector.IntegrityError as e:
            flash("Error: This ID already exists. Please use a unique ID.", "error")
        return redirect(url_for('Index'))

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method=='POST':
        # init_id = request.form['id']
        id = request.form['idnum']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        course = request.form['course']
        year = request.form['year']
        gender = request.form['gender']
        
        models.Students.editStudent(id, firstname, lastname, course, year, gender)
        flash("Data Updated Successfully!")
        mysql_conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete(id):
    models.Students.deleteStudent(id)
    flash("Data deleted Successfully!")
    return redirect(url_for('Index'))

@app.route('/college')
def college():

    data = models.Colleges.collegeData()
    return render_template('college.html', colleges =data)

@app.route('/insert-college', methods = ['POST'])
def insert_college():
    if request.method == "POST":
        try:
            code = request.form['code']
            name = request.form['name']
            models.Colleges.addCollege(code, name)
            flash("Data inserted successfully!", "success")
        except mysql.connector.IntegrityError as e:
            flash("Error: This ID already exists. Please use a unique ID.", "error")        
        return redirect(url_for('college'))

@app.route('/update-college', methods=['POST', 'GET'])
def update_college():
    if request.method=='POST':
        # init_id = request.form['id']
        code = request.form['code']
        name = request.form['name']

        cursor = mysql_conn.cursor()
        models.Colleges.addCollege(code, name)  

        flash("Data Updated Successfully!")
        mysql_conn.commit()
        return redirect(url_for('college'))    
    
@app.route('/delete_college/<string:id>', methods=['POST', 'GET'])
def delete_college(id):
    models.Colleges.deleteCollege(id)
    
    flash("Data deleted Successfully!")
    return redirect(url_for('college'))

@app.route('/course')
def course():

    data = models.Courses.courseData()
    data1 = models.Colleges.collegeData()
    cursor.close()

    return render_template('course.html', courses =data, colleges=data1)

@app.route('/insert-course', methods = ['POST'])
def insert_course():
    if request.method == "POST":
        try:
            code = request.form['course_code']
            name = request.form['course_name']
            college_code = request.form['college']

            models.Courses.addCourse(code, name, college_code)
            flash("Data inserted successfully!", "success")

        except mysql.connector.IntegrityError as e:
            flash("Error: This ID already exists. Please use a unique ID.", "error")        
        return redirect(url_for('course'))

@app.route('/update-course', methods=['POST', 'GET'])
def update_course():
    if request.method=='POST':
        # init_id = request.form['id']
        code = request.form['course_code']
        name = request.form['course_name']
        college_code = request.form['college']

        models.Courses.addCourse(code, name, college_code)

        flash("Data Updated Successfully!")
        mysql_conn.commit()
        return redirect(url_for('course'))    
    
@app.route('/delete_course/<string:id>', methods=['POST', 'GET'])
def delete_course(id):
    models.Courses.deleteCourse(id)
    
    flash("Data deleted Successfully!")
    return redirect(url_for('course'))

if __name__ == "__main__":
    app.run(debug=True)
