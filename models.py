from app import mysql

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

    def addStudent(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO student(id,firstname,lastname,course_code,year,gender) \
                VALUES('{self.id}','{self.firstname}','{self.lastname}','{self.course_code}','{self.year}','{self.gender}')"
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()

    def editStudent(self):
        cursor = mysql.connection.cursor()
        print(self.id)

        sql = f"UPDATE student SET id ='{self.id}',firstname ='{self.firstname}',lastname ='{self.lastname}'," \
                f"course_code ='{self.course_code}',year_level ='{self.year}'," \
                f"gender ='{self.gender}' WHERE id_number = '{self.oldid}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connection.commit()

    @classmethod
    def studentData(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deleteStudent(cls, id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from student where id = '{id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchStudent(cls, id):
        cursor = mysql.connection.cursor()
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

    def addCourse(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO course(code,name,college_code) \
                VALUES('{self.code}','{self.name}','{self.college_code}')"
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()

    def editCourse(self):
        cursor = mysql.connection.cursor()
        print(self.code)
        sql = f"UPDATE course SET code ='{self.code}', name ='{self.name}',college_code ='{self.college_code}'" \
              f"WHERE code = '{str(self.oldcode)}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connection.commit()

    @classmethod
    def courseData(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deleteCourse(cls, code):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE FROM course where code = '{code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchCourse(cls, code):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from course where code='{code}'"
        cursor.execute(sql)
        codes = cursor.fetchall()
        return codes

class College(object):

    def __init__(self, code = None, name = None, oldcode = None):
        self.code = code
        self.name = name
        self.oldcode = oldcode

    def addCollege(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO college(code, name) \
                VALUES('{self.code}','{self.name}')"
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()

    def editCollege(self):
        cursor = mysql.connection.cursor()
        print(self.code)
        sql = f"UPDATE college SET code ='{self.code}', name ='{self.name}' WHERE code = '{str(self.oldcode)}'"
        print(sql)
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connection.commit()

    @classmethod
    def collegeData(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deleteCollege(cls, code):
        try:
            print(code, "code delete")
            cursor = mysql.connection.cursor()
            sql = f"DELETE from college where code = '{code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchCollege(cls, code):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from college where code='{code}'"
        print(sql, "SEARCH COLLEGE")
        cursor.execute(sql)
        codec = cursor.fetchall()
        return codec