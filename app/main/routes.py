from flask import render_template, Blueprint, flash, redirect, url_for, request
from flask_login import login_required, current_user, logout_user
from app import db
from app.main import main
from app.main.forms import UpdateAccountForm
from app.models import AirQualityData, User

@main.route("/")
@main.route("/index")
def index():
    return render_template('main/index.html', title='Home')

@main.route("/dashboard")
@login_required
def dashboard():
    # Fetch some dummy data for the dashboard
    data = AirQualityData.query.order_by(AirQualityData.timestamp.desc()).limit(10).all()
    return render_template('main/dashboard.html', title='Dashboard', data=data)

@main.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('main/profile.html', title='Profile', form=form)

@main.route("/account/delete", methods=['POST'])
@login_required
def delete_account():
    user = User.query.get(current_user.id) # Get actual user object, not proxy
    db.session.delete(user)
    db.session.commit()
    logout_user() # Logout after deletion
    flash('Your account has been deleted.', 'info')
    return redirect(url_for('main.index'))
