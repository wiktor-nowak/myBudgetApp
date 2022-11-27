from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, FloatField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length, InputRequired


# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     # remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign IN')
#
#
# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
#     # remember_me = BooleanField('Remember Me')
#     submit = SubmitField('REGISTER')

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different username.')
    #
    # def validate_email(self, email):
    #     emailaddress = User.query.filter_by(email=email.data).first()
    #     if emailaddress is not None:
    #         raise ValidationError('Please use a different e-mail address.')


class AddExpense(FlaskForm):
    spender = SelectField('Name', choices=[], validators=[DataRequired()])
    category = SelectField('Category', choices=[], validators=[DataRequired()])
    amount = FloatField('Amount', validators=[InputRequired()])
    account = SelectField('Account', choices=[], validators=[DataRequired()])
    description = TextAreaField('Notes')
    submit = SubmitField('ADD')
