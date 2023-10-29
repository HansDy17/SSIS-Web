from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from datetime import datetime # add the date of college added
from .models import *
#from college_bp import mysql

college_bp = Blueprint('college_bp', __name__)

@college_bp.route('/college')
def college():

    data =  Colleges.collegeData()
    return render_template('college.html', colleges =data)

@college_bp.route('/insert-college', methods = ['POST'])
def insert_college():
    if request.method == "POST":
        try:
            code = request.form['code']
            name = request.form['name']
            Colleges.addCollege(code, name)
            flash("Data inserted successfully!", "success")
        except mysql.connector.IntegrityError as e:
            flash("Error: This ID already exists. Please use a unique ID.", "error")        
        return redirect(url_for('college_bp.college'))

@college_bp.route('/update-college', methods=['POST', 'GET'])
def update_college():
    if request.method=='POST':
        # init_id = request.form['id']
        code = request.form['code']
        name = request.form['name']

        Colleges.editCollege(code, name)  

        flash("Data Updated Successfully!")

        return redirect(url_for('college_bp.college'))    
    
@college_bp.route('/delete_college/<string:id>', methods=['POST', 'GET'])
def delete_college(id):
    Colleges.deleteCollege(id)
    
    flash("Data deleted Successfully!")
    return redirect(url_for('college_bp.college'))