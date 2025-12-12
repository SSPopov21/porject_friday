from flask import render_template, Blueprint, flash, redirect, url_for, request
from flask_login import login_required, current_user, logout_user
from app import db
from app.main import main
from app.main.forms import UpdateAccountForm, DataForm
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

@main.route("/data/new", methods=['GET', 'POST'])
@login_required
def new_data():
    form = DataForm()
    if form.validate_on_submit():
        # Simple anomaly detection logic (could be moved to AI module)
        anomaly = 0.0
        if form.pm25.data > 50 or form.co2.data > 1000:
            anomaly = 1.0
            
        data = AirQualityData(
            pm25=form.pm25.data,
            pm10=form.pm10.data,
            co2=form.co2.data,
            anomaly_score=anomaly
        )
        db.session.add(data)
        db.session.commit()
        flash('New reading added!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('main/add_data.html', title='Add Data', form=form)

@main.route("/data/<int:data_id>/delete", methods=['POST'])
@login_required
def delete_data(data_id):
    data = AirQualityData.query.get_or_404(data_id)
    db.session.delete(data)
    db.session.commit()
    flash('Reading deleted.', 'success')
    return redirect(url_for('main.dashboard'))
