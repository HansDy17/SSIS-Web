from flask import Flask
#from flask_mysql_connector import MySQL
# from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL, CLOUD_NAME, API_KEY, API_SECRET
# from flask_wtf.csrf import CSRFProtect
import cloudinary
import cloudinary.api
import cloudinary.uploader

# mysql = MySQL()
# bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST, 
        BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
          
    cloudinary.config( 
    cloud_name = CLOUD_NAME, 
    api_key = API_KEY, 
    api_secret = API_SECRET 
    )
    # bootstrap.init_app(app)
    #mysql.init_app(app)
    # CSRFProtect(app)

    from .controller import student_bp
    from .college import college_bp
    from .course import course_bp

    app.register_blueprint(student_bp, url_prefix='/')
    app.register_blueprint(college_bp, url_prefix='/')
    app.register_blueprint(course_bp, url_prefix='/')

    return app
