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
            cursor = mysql.connection.cursor()
            database = "INSERT INTO contact (name, email) VALUES (%s, %s)"
            val = (name, email)
            cursor.execute(database,val)
            mysql.connection.commit()
            cursor.close()

            msg = Message(
                'Thank you for joining ChidoLingo Promos Mailing List',
                sender='chidopromos@gmail.com',
                recipients=[email]
            )
            msg.html = render_template(template_name_or_list="email-maillist.html")
            mail.send(msg)
            return render_template("signupconfirmation.html", name=name, email=email)

    else:
        return render_template("signup.html", form=cform)


###############################################
#                Run application                      #
###############################################

if __name__ == '__main__':
    application.debug = True
    application.run()