from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email

#Similar to making an instance of the flask object app = Flask(__name__)
users = Blueprint('users', __name__)

@users.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()


        #Note, success indicates the styling - the bootstrap class - to use for the flash message (i.e. green or red border)
        flash(f'Your account has been created. You are now able to log in!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title = 'Register', form = form)

@users.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


#Including the login_required decorator here is important because it allows Flask to know...
#...which pages should only be accessible to users that are logged in.
@users.route('/account', methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            #This conditional is saying: "If the user has uploaded a new file, 
            # ...then set the image file as that new file."
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account details have been updated.', 'success')

        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
    
    return render_template('account.html', title = 'Account', image_file = image_file, form = form)

@users.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type = int)

    #Find the posts of this user, or 404 if the user does not exist.
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author = user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page = page, per_page=2)
    return render_template('user_posts.html', posts=posts, user=user)

@users.route("/reset_password", methods =["GET","POST"])
def reset_request():
    #To make sure that the user is logged out.
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email containing instructions on how to reset your password has been sent.", 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title = 'Reset Password', form = form)


@users.route("/reset_password/<token>", methods =["GET","POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    #Pass in the token from the url, also... 
    # the method is inherited from the static method in models.py for User
    user = User.verify_reset_token(token)

    #Check if the token is valid and if the user was verified via the token.
    if user is None:
        flash("That is an invalid or expired token", 'warning')
        return redirect(url_for('users.reset_request'))

    
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #user is already in the database and given by the verify token method.
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been updated. You are now able to log in with your new password', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title = 'Reset Password', form = form)
