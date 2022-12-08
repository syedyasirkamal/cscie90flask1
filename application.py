#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from models import signupForm


###############################################
#          Define flask application                   #from flaskapplication import db, Contact
###############################################

application = Flask(__name__,template_folder='templates')
application.secret_key = 'the random string'
Bootstrap(application)



###############################################
#         Database connection info
###############################################


application.config['MYSQL_HOST'] = 'flask-application.cpetmtsmol3b.us-east-1.rds.amazonaws.com'
application.config['MYSQL_USER'] = 'admin'
application.config['MYSQL_PASSWORD'] = '123abcde'
application.config['MYSQL_PORT'] = 3306
application.config['MYSQL_DB'] = 'sys'
application.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(application)

###############################################
#         Flask Mail application
###############################################

# configuration of mail
application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USERNAME'] = 'chidopromos@gmail.com'
application.config['MAIL_PASSWORD'] = 'onzzqwzrobdsmcna'
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True
mail = Mail(application)


@application.route('/createdatabase')
def createdatabase():
    # Creating a connection cursor
    cursor = mysql.connection.cursor()

    # Executing SQL Statements
    #cursor.execute('''CREATE TABLE contact (id INTEGER, name VARCHAR(50), email VARCHAR(100), message VARCHAR(2000), date_created TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL, PRIMARY KEY (id))''')

    # Saving the Actions performed on the DB
    mysql.connection.commit()

    # Closing the cursor
    cursor.close()
    return 'done!'


###############################################
#       Render Contact page                   #
###############################################

@application.route("/")
def root():
    return render_template("index.html")



###############################################
#                Run application                      #
###############################################

if __name__ == '__main__':
    application.debug = True
    application.run()