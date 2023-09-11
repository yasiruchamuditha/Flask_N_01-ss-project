from flask_wtf import FlaskForm
from wtforms import  StringField , PasswordField , SubmitField , SelectField
from wtforms.validators import DataRequired,Email,EqualTo

class RegistrationForm(FlaskForm):
    userEmail = StringField('userEmail',validators=[DataRequired(),Email()])
    userRole = SelectField('userRole',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField ('signup')

class LoginForm(FlaskForm):
    userEmail = StringField('userEmail',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField ('signin')




    