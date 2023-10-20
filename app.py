from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime # add the date of student added

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
    cursor = mysql_conn.cursor()
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM course")
    data1 = cursor.fetchall()

    cursor.close()

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

            cursor.execute("INSERT INTO student(id, firstname, lastname, course_code, year, gender) VALUES(%s, %s, %s, %s, %s, %s)", (id, firstname, lastname, course, year, gender))
            mysql_conn.commit()
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

        cursor = mysql_conn.cursor()
        cursor.execute("UPDATE student SET id=%s, firstname=%s, lastname=%s, course_code=%s, year=%s, gender=%s WHERE id =%s", (id, firstname, lastname, course, year, gender, id))

        flash("Data Updated Successfully!")
        mysql_conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete(id):
    cursor = mysql_conn.cursor()
    cursor.execute('DELETE FROM student WHERE id = %s', (id,))
    mysql_conn.commit()
    
    flash("Data deleted Successfully!")
    return redirect(url_for('Index'))

@app.route('/college')
def college():
    cursor = mysql_conn.cursor()
    cursor.execute("SELECT * FROM college")
    data = cursor.fetchall()
    cursor.close()

    return render_template('college.html', colleges =data)

@app.route('/insert-college', methods = ['POST'])
def insert_college():
    if request.method == "POST":
        try:
            code = request.form['code']
            name = request.form['name']

            cursor.execute("INSERT INTO college(code, name) VALUES(%s, %s)", (code, name))
            mysql_conn.commit()
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
        cursor.execute("UPDATE college SET code=%s, name=%s WHERE code =%s", (code, name, code))

        flash("Data Updated Successfully!")
        mysql_conn.commit()
        return redirect(url_for('college'))    
    
@app.route('/delete_college/<string:id>', methods=['POST', 'GET'])
def delete_college(id):
    cursor = mysql_conn.cursor()
    cursor.execute('UPDATE course SET college_code = NULL WHERE college_code = %s', (id,))
    cursor.execute('DELETE FROM college WHERE code = %s', (id,))

    mysql_conn.commit()
    
    flash("Data deleted Successfully!")
    return redirect(url_for('college'))

@app.route('/course')
def course():
    cursor = mysql_conn.cursor()
    cursor.execute("SELECT * FROM course")
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM college")
    data1 = cursor.fetchall()
    cursor.close()

    return render_template('course.html', courses =data, colleges=data1)

@app.route('/insert-course', methods = ['POST'])
def insert_course():
    if request.method == "POST":
        try:
            course_code = request.form['course_code']
            name = request.form['course_name']
            college_code = request.form['college']

            cursor.execute("INSERT INTO course(code, name, college_code) VALUES(%s, %s, %s)", (course_code, name, college_code))
            mysql_conn.commit()
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

        cursor = mysql_conn.cursor()
        cursor.execute("UPDATE course SET code=%s, name=%s, college_code=%s WHERE code =%s", (code, name, college_code, code))

        flash("Data Updated Successfully!")
        mysql_conn.commit()
        return redirect(url_for('course'))    
    
@app.route('/delete_course/<string:id>', methods=['POST', 'GET'])
def delete_course(id):
    cursor = mysql_conn.cursor()
    cursor.execute('UPDATE student SET course_code = NULL WHERE course_code = %s', (id,))
    cursor.execute('DELETE FROM course WHERE code = %s', (id,))
    mysql_conn.commit()
    
    flash("Data deleted Successfully!")
    return redirect(url_for('course'))

if __name__ == "__main__":
    app.run(debug=True)
