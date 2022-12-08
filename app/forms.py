from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField,  SelectField
from wtforms.validators import DataRequired
from app.classes import Email, Date_Time, Name_Validation
from wtforms.fields import DateTimeField

class signupForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(), Name_Validation.validate_name])
    email = StringField(label='Email', validators=[
        DataRequired(), Email(granular_message=True)])
    submit = SubmitField(label="Test Form")