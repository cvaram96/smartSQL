from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User
from flask_login import current_user
class RegistrationForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',
		validators=[DataRequired(),Length(min=2,max=20),Email()]) 
	password = PasswordField('password',
		validators=[DataRequired(),Length(min=5)])
	confirm_password = PasswordField('confirm password',
		validators=[DataRequired(),Length(min=5),EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		if current_user.is_authenticated:
			if username.data != current_user.username:
				user = User.query.filter_by(username= username.data).first()
				if user:
					raise ValidationError('That username is already taken!')
		else:
			user = User.query.filter_by(username= username.data).first()
			if user:
				raise ValidationError('That username is already taken!')
	
	def validate_email(self, email):
		if current_user.is_authenticated:
			if email.data != current_user.email:
				user = User.query.filter_by(email= email.data).first()
				if user:
					raise ValidationError('That email is already taken!')
		else:
			user = User.query.filter_by(email= email.data).first()
			if user:
				raise ValidationError('That email is already taken!')


class LoginForm(FlaskForm):
	
	email = StringField('Email',
		validators=[DataRequired(),Length(min=2,max=20),Email()]) 
	password = PasswordField('password',
		validators=[DataRequired(),Length(min=5)])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Log In')

class UpdateAccountForm(FlaskForm):

	username = StringField('Username',
		validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',
		validators=[DataRequired(),Length(min=2,max=20),Email()])
	picture = FileField('Update profile picture',
		validators = [FileAllowed(['jpg','jpeg','png'])]) 
	submit = SubmitField('Update')

	def validate_username(self, username):
		if current_user.is_authenticated:
			if username.data != current_user.username:
				user = User.query.filter_by(username= username.data).first()
				if user:
					raise ValidationError('That username is already taken!')
		else:
			user = User.query.filter_by(username= username.data).first()
			if user:
				raise ValidationError('That username is already taken!')
	
	def validate_email(self, email):
		if current_user.is_authenticated:
			if email.data != current_user.email:
				user = User.query.filter_by(email= email.data).first()
				if user:
					raise ValidationError('That email is already taken!')
		else:
			user = User.query.filter_by(email= email.data).first()
			if user:
				raise ValidationError('That email is already taken!')


class insertDumpDatabaseForm(FlaskForm):
	title =StringField('Database name', validators=[DataRequired()])

	dumpFile = FileField('Update your new dumped database file ',
		validators = [FileAllowed(['sql'])]) 

	submit = SubmitField('upload')


class PostForm(FlaskForm):
	title = StringField('Title',validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('submit')

class QueryForm(FlaskForm):
	userQuery = TextAreaField('Your natural language Query', validators=[DataRequired()])
	systemQuery = TextAreaField('Corresponding SQL Query', validators=[])
	submit = SubmitField('submit')
