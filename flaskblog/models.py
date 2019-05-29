from datetime import datetime
from flaskblog import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model,UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20),unique = True, nullable = False)
	email = db.Column(db.String(120),unique = True, nullable = False)
	image_file = db.Column(db.String(20),unique = False, nullable =True,default = 'default.png')
	password = db.Column(db.String(60), nullable = False)
	posts = db.relationship('Post', backref = 'author', lazy=True)
	databases = db.relationship('Database',backref = 'owner', lazy = True)
	
	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), nullable = False)
	data_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable =False)

	def __repr__(self):
		return f"User('{self.title}','{self.data_posted}','{self.image_file}')"

class Database(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), nullable = False)
	database_file = db.Column(db.String(20),unique = False, nullable =False)
	data_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable =False)



