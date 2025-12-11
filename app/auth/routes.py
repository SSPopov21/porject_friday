import datetime
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app import db
from app.models import User
from app.auth import auth
from app.auth.forms import RegistrationForm, LoginForm

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # Simulation of sending email
        # In a real app, generate a token and send an email
        # For now, we will leave the user unconfirmed and show a message
        flash(f'Account created for {form.username.data}! Please check your email to verify your account.', 'success')
        
        # Simulating verification link display (for MVP purpose)
        print(f"DEBUG: To verify account, go to /auth/confirm_email/{form.email.data}") 
        
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            # Check if confirmed
            if not user.confirmed:
                flash('Please verify your account first.', 'warning')
                return redirect(url_for('auth.login'))
                
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('auth/login.html', title='Login', form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route("/confirm_email/<email>")
def confirm_email(email):
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
         flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('auth.login'))
