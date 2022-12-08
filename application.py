#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, email


class signupForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[
        DataRequired(), email()])
    submit = SubmitField(label="Test Form")


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
#         Flask Mail App
###############################################

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'chidopromos@gmail.com'
app.config['MAIL_PASSWORD'] = 'onzzqwzrobdsmcna'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/createdatabase')
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




@app.route('/signup', methods=["GET", "POST"])
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
#                Run app                      #
###############################################

if __name__ == '__main__':
    app.debug = True
    app.run()