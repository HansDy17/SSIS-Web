from app import mysql
import mysql.connector

#from werkzeug.security import generate_password_hash, check_password_hash

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

    def addStudent(self,id, first, last, course, year, gender):
        cursor = mysql.connector.cursor()
        sql = f"INSERT INTO student(id,firstname,lastname,course_code,year,gender) \
                VALUES('{id}','{first}','{last}','{course}','{year}','{gender}')"
        print(sql)
        cursor.execute(sql)
        mysql.connector.commit()

    def editStudent(self, id, first, last, course, year, gender):
        cursor = mysql.connector.cursor()
        print(self.id)

        sql = f"UPDATE student SET id ='{id}',firstname ='{first}',lastname ='{last}'," \
                f"course_code ='{course}',year_level ='{year}'," \
                f"gender ='{gender}' WHERE id_number = '{id}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connector.commit()

    @classmethod
    def studentData(cls):
        cursor = mysql.connector.cursor()
        sql = "SELECT * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deleteStudent(cls, id):
        try:
            cursor = mysql.connector.cursor()
            sql = f"DELETE from student where id = '{id}'"
            cursor.execute(sql)
            mysql.connector.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchStudent(cls, id):
        cursor = mysql.connector.cursor()
        sql = f"SELECT * from student where id='{id}'"
        cursor.execute(sql)
        ids = cursor.fetchall()
        return ids

class Courses(object):

    def __init__(self, code = None, name = None, college_code = None, oldcode = None):
        self.code = code
        self.name = name
        self.college_code = college_code
        self.oldcode = oldcode

    def addCourse(self, code, name, ccode):
        cursor = mysql.connector.cursor()
        sql = f"INSERT INTO course(code,name,college_code) \
                VALUES('{code}','{name}','{ccode}')"
        print(sql)
        cursor.execute(sql)
        mysql.connector.commit()

    def editCourse(self, code, name, ccode):
        cursor = mysql.connector.cursor()
        print(self.code)
        sql = f"UPDATE course SET code ='{code}', name ='{name}',college_code ='{ccode}'" \
              f"WHERE code = '{str(code)}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connector.commit()

    @classmethod
    def courseData(cls):
        cursor = mysql.connector.cursor()
        sql = "SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deleteCourse(cls, code):
        try:
            cursor = mysql.connector.cursor()
            sql = f"DELETE FROM course where code = '{code}'"
            cursor.execute(sql)
            mysql.connector.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchCourse(cls, code):
        cursor = mysql.connector.cursor()
        sql = f"SELECT * from course where code='{code}'"
        cursor.execute(sql)
        codes = cursor.fetchall()
        return codes

class Colleges(object):

    def __init__(self, code = None, name = None, oldcode = None):
        self.code = code
        self.name = name
        self.oldcode = oldcode

    def addCollege(self, code, name):
        cursor = mysql.connector.cursor()
        sql = f"INSERT INTO college(code, name) \
                VALUES('{code}','{name}')"
        print(sql)
        cursor.execute(sql)
        mysql.connector.commit()

    def editCollege(self, code, name):
        cursor = mysql.connector.cursor()
        print(self.code)
        sql = f"UPDATE college SET code ='{code}', name ='{name}' WHERE code = '{str(code)}'"
        print(sql)
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connector.commit()

    @classmethod
    def collegeData(cls):
        cursor = mysql.connector.cursor()
        sql = "SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deleteCollege(cls, code):
        try:
            print(code, "code delete")
            cursor = mysql.connector.cursor()
            sql = f"DELETE from college where code = '{code}'"
            cursor.execute(sql)
            mysql.connector.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchCollege(cls, code):
        cursor = mysql.connector.cursor()
        sql = f"SELECT * from college where code='{code}'"
        print(sql, "SEARCH COLLEGE")
        cursor.execute(sql)
        codec = cursor.fetchall()
        return codec