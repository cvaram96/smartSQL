import secrets
import os
from flask import render_template, url_for, flash, redirect, request, abort
#from PIL import Image
from flaskblog import app,db, bcrypt
from flaskblog.forms import *
from flaskblog.models import *
from flask_login import login_user, current_user,logout_user,login_required
from flaskblog.ln2sql.ln2sql import Ln2sql
from flaskblog.ln2sql.database import Database as Data_object
@app.route("/")
def home():
	posts = Post.query.all()
	return render_template('home.html',posts=posts)

@app.route("/about")
def about():
	return render_template('about.html',title = 'about')

@app.route("/register", methods = ['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form= RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, email=form.email.data, password = hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.username.data}!... you are able to login','success')
		login_user(user,force =True)
		return redirect(url_for('account'))
	return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods =['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form= LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,remember = form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash(f'Login is unsuccesful, please check your email or password','danger')

	return render_template('login.html', title = 'Login', form = form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	name,f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex+f_ext
	picture_path = os.path.join(app.root_path,'static/profile_pics',picture_fn)
	form_picture.save(picture_path)
	return picture_fn	



@app.route("/account",methods =['GET','POST'])
@login_required
def account():
	databases=[]
	listdatabase = Database.query.all()
	for l in listdatabase:
		if l.owner == current_user:
			databases.append(l)
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.email= form.email.data
		db.session.commit()
		flash('your account is successfully updated','success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data=current_user.username
		form.email.data=current_user.email
	image_file = url_for('static',filename='profile_pics/'+ current_user.image_file)
	return render_template('account.html', title = 'account', image_file = image_file, form =form , databases = databases)


def save_database(form_picture):
	random_hex = secrets.token_hex(8)
	f_name,f_ext = os.path.splitext(form_picture.filename)
	db_fn = random_hex+f_ext
	db_path = os.path.join(app.root_path,'ln2sql/database_store',db_fn)
	form_picture.save(db_path)
	return db_fn




@app.route("/smartSQL",methods =['GET','POST'])
@login_required
def dumpSQL():
	form = insertDumpDatabaseForm()
	if form.validate_on_submit():
		if form.dumpFile.data:
			dump_file = save_database(form.dumpFile.data)
			dump_db = Database(title= form.title.data, database_file = dump_file, owner = current_user)
			db.session.add(dump_db)
			db.session.commit()
		flash(f'your database is successfully updated','success')
		return redirect(url_for('account'))
	return render_template('smartSQL.html', title = 'file', form =form)


@app.route("/post/new",methods =['GET','POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title = form.title.data, content = form.content.data, author = current_user)
		db.session.add(post)
		db.session.commit()
		flash(f'your post has been created','success')
		return redirect(url_for('home'))
	return render_template('create_post.html', title = 'new post', legend = 'Review about product',form = form)


@app.route("/post/<int:post_id>", methods =['GET','POST'])
def post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('post.html',title =post.title, post =post)

@app.route("/post/<int:post_id>/update", methods =['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Review')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Your post has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route("/database/<int:database_id>", methods =['GET','POST'])
def database(database_id):

	database = Database.query.get_or_404(database_id)
	form = QueryForm()
	database_file = 'database_store/'+ database.database_file
	queryLoader = Ln2sql(database_file,'lang_store/english.csv')
	database_object = Data_object()
	database_object.load(database_file)
	database_container = database_object.get_tables_into_dictionary()
	Query=''
	sql=''
	length = 12/len(database_container)
	partition_string = "col-"+str(int(length))
	print(partition_string)
	if form.validate_on_submit():
		Query =form.userQuery.data
		sql=queryLoader.get_query(Query)
		if(type(sql) == str):
			form.systemQuery.data =sql
		else:
			form.systemQuery.data = 'Your Query has not follow the instructions'


		return render_template('database.html',title =database.title, database =database, container = database_container, form = form,partition_string = partition_string)


	elif request.method == 'GET':
		form.userQuery.data =Query
		form.systemQuery.data =sql

	return render_template('database.html',title =database.title, database =database, form = form, container = database_container, partition_string = partition_string)


@app.route("/database/<int:database_id>/delete", methods=['POST'])
@login_required
def delete_database(database_id):
    database = Database.query.get_or_404(database_id)
    if database.owner != current_user:
        abort(403)
    db.session.delete(database)
    db.session.commit()
    flash('Your database has been deleted!', 'success')
    return redirect(url_for('account'))