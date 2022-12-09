#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from models import signupForm


###############################################
#          Define flask app                   #from flaskapp import db, Contact
###############################################

app = Flask(__name__,template_folder='templates')
app.secret_key = 'the random string'
Bootstrap(app)



###############################################
#         Database connection info
###############################################


app.config['MYSQL_HOST'] = 'flask-app.cpetmtsmol3b.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '123abcde'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'sys'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

###############################################
#         Flask Mail app
###############################################



###############################################
#       Render Contact page                   #
###############################################




@app.route('/', methods=["GET", "POST"])
def home():
    cform = signupForm()
    return render_template("signup.html", form=cform)


@app.route('/signup/submit', methods=['POST', 'GET'])
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
#                Run app                      #
###############################################

if __name__ == '__main__':
    app.debug = True
    app.run()