#          Import some packages               #
###############################################
from flask import Flask, render_template, request
import MySQLdb
from flask_bootstrap import Bootstrap
from models import signupForm


###############################################
#          Define flask application                   #from flaskapplication import db, Contact
###############################################

application = Flask(__name__)
Bootstrap(application)


###############################################
#         Database connection info
###############################################


db = MySQLdb.connect(host="flask-application.cpetmtsmol3b.us-east-1.rds.amazonaws.com",
                     port=3306,
                     user="admin",
                     passwd="123abcde",
                     db="sys",
                     autocommit=True,
                     use_unicode=True
                     )

###############################################
#       Render Contact page                   #
###############################################

@application.route("/")
def root():
    return render_template("index.html")


@application.route('/signup', methods=["GET", "POST"])
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
            cursor = db.cursor()
            database = "INSERT INTO contact (name, email) VALUES (%s, %s)"
            val = (name, email)
            cursor.execute(database, val)
            cursor.close()
            return render_template("signupconfirmation.html", name=name, email=email)
    else:
        return render_template("signup.html", form=cform)


###############################################
#                Run application                      #
###############################################

if __name__ == '__main__':
    application.debug = True
    application.run()

