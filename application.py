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