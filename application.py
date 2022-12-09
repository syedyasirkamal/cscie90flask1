#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
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


application.config['MYSQL_HOST'] = 'awseb-e-r3pvnbrmxr-stack-awsebrdsdatabase-lh00miqeio2a.cpetmtsmol3b.us-east-1.rds.amazonaws.com'
application.config['MYSQL_USER'] = 'admin'
application.config['MYSQL_PASSWORD'] = '123abcde'
application.config['MYSQL_PORT'] = 3306
application.config['MYSQL_DB'] = 'ebdb'
application.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(application)

###############################################
#         Flask Mail application
###############################################

@application.route('/createdatabase')
def createdatabase():
    # Creating a connection cursor
    cursor = mysql.connection.cursor()

    # Executing SQL Statements
    cursor.execute('''CREATE TABLE contact (id INTEGER, name VARCHAR(50), email VARCHAR(100), message VARCHAR(2000), date_created TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL, PRIMARY KEY (id))''')
    #cursor.execute('''CREATE TABLE trial (id INTEGER, firstname VARCHAR(50), lastname VARCHAR(50), email VARCHAR(100), tutor VARCHAR(100), datetime  DATETIME, date_created TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL, PRIMARY KEY (id))''')

    # Saving the Actions performed on the DB
    mysql.connection.commit()

    # Closing the cursor
    cursor.close()
    return 'done!'


###############################################
#       Render Contact page                   #
###############################################




@application.route('/', methods=["GET", "POST"])
def home():
    cform = signupForm()
    return render_template("signup.html", form=cform)


@application.route('/signup/submit', methods=['POST', 'GET'])
def signupsubmit():
    if request.method == 'GET':
        return "Login via the login Form"
    cform = signupForm()
    if cform.validate_on_submit():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            cursor = mysql.connection.cursor()
            database = "INSERT INTO contact (name, email) VALUES (%s, %s)"
            val = (name, email)
            cursor.execute(database,val)
            mysql.connection.commit()
            cursor.close()

            return render_template("signupconfirmation.html", name=name, email=email)

    else:
        return render_template("signup.html", form=cform)


###############################################
#                Run application                      #
###############################################

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080, debug=True)