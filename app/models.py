#from app import mysql
import mysql.connector

#from werkzeug.security import generate_password_hash, check_password_hash

db_conn = mysql.connector.connect(
    host='localhost',
    user="root",
    password="1234",
    database="ssis_web"
)

# Create a cursor from the database connection
cursor = db_conn.cursor()


class Students(object):

    def __init__(self, id = None, firstname = None, lastname = None, course_code = None,
                 year = None, gender = None, oldid = None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.course_code = course_code
        self.year = year
        self.gender = gender
        self.oldid = oldid

    def addStudent(id, first, last, course, year, gender):
        cursor = db_conn.cursor()
        sql = f"INSERT INTO student(id,firstname,lastname,course_code,year,gender) \
                VALUES('{id}','{first}','{last}','{course}','{year}','{gender}')"
        print(sql)
        cursor.execute(sql)
        db_conn.commit()
        cursor.close()

    def editStudent(id, first, last, course, year, gender):
        cursor = db_conn.cursor()
        print(id)

        sql = f"UPDATE student SET id ='{id}',firstname ='{first}',lastname ='{last}'," \
                f"course_code ='{course}',year ='{year}'," \
                f"gender ='{gender}' WHERE id = '{id}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        db_conn.commit()
        cursor.close()


    @classmethod
    def studentData(cls):
        cursor = db_conn.cursor()
        sql = "SELECT * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    @classmethod
    def deleteStudent(cls, id):
        try:
            cursor = db_conn.cursor()
            sql = f"DELETE from student where id = '{id}'"
            cursor.execute(sql)
            db_conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            db_conn.rollback()  # Rollback the transaction on error
            return False
        finally:
            cursor.close()

    def searchStudent(cls, id):
        cursor = db_conn.cursor()
        sql = f"SELECT * from student where id='{id}'"
        cursor.execute(sql)
        ids = cursor.fetchall()
        cursor.close()
        return ids

class Courses(object):

    def __init__(self, code = None, name = None, college_code = None, oldcode = None):
        self.code = code
        self.name = name
        self.college_code = college_code
        self.oldcode = oldcode

    def addCourse(code, name, ccode):
        cursor = db_conn.cursor()
        sql = f"INSERT INTO course(code,name,college_code) \
                VALUES('{code}','{name}','{ccode}')"
        print(sql)
        cursor.execute(sql)
        db_conn.commit()
        cursor.close()

    def editCourse(code, name, ccode):
        cursor = db_conn.cursor()
        print(code)
        sql = f"UPDATE course SET code ='{code}', name ='{name}',college_code ='{ccode}'" \
              f"WHERE code = '{str(code)}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        db_conn.commit()
        cursor.close()

    @classmethod
    def courseData(cls):
        cursor = db_conn.cursor()
        sql = "SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    @classmethod
    def deleteCourse(cls, code):
        try:
            cursor = db_conn.cursor()
            sql = f"DELETE FROM course where code = '{code}'"
            sql2 =f" UPDATE student SET course_code = NULL WHERE course_code ='{code}'"
            cursor.execute(sql2)
            cursor.execute(sql)  
            db_conn.commit()
            return True
        except Exception as e:
            print(e)
            db_conn.rollback()  # Rollback the transaction on error
            return False
        finally:
            cursor.close()
            

    def searchCourse(cls, code):
        cursor = db_conn.cursor()
        sql = f"SELECT * from course where code='{code}'"
        cursor.execute(sql)
        codes = cursor.fetchall()
        cursor.close()
        return codes

class Colleges(object):

    def __init__(self, code = None, name = None, oldcode = None):
        self.code = code
        self.name = name
        self.oldcode = oldcode

    def addCollege(code, name):
        cursor = db_conn.cursor()
        sql = f"INSERT INTO college(code, name) \
                VALUES('{code}','{name}')"
        print(sql)
        cursor.execute(sql)
        db_conn.commit()
        cursor.close()

    def editCollege(code, name):
        cursor = db_conn.cursor()
        print(code)
        sql = f"UPDATE college SET code ='{code}', name ='{name}' WHERE code = '{str(code)}'"
        print(sql)
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        db_conn.commit()
        cursor.close()

    @classmethod
    def collegeData(cls):
        cursor = db_conn.cursor()
        sql = "SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    @classmethod
    def deleteCollege(cls, code):
        try:
            print(code, "code delete")
            cursor = db_conn.cursor()
            sql = f"DELETE from college where code = '{code}'"
            sql2 =f" UPDATE course SET college_code = NULL WHERE college_code ='{code}'"
            cursor.execute(sql2)
            cursor.execute(sql)            
            db_conn.commit()
            return True
        except Exception as e:
            print(e)
            db_conn.rollback()  # Rollback the transaction on error
            return False
        finally:
            cursor.close()

    def searchCollege(cls, code):
        cursor = db_conn.cursor()
        sql = f"SELECT * from college where code='{code}'"
        print(sql, "SEARCH COLLEGE")
        cursor.execute(sql)
        codec = cursor.fetchall()
        cursor.close()
        return codec