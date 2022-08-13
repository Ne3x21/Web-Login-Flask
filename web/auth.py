from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import recaptcha, db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if recaptcha.verify():
            email = request.form.get('email')
            password = request.form.get('password')

            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash('Incorrect password.', category='error')
            else:
                flash('Email dose not exist.', category='error')
        else:
            flash('ReCaptcha required!', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        if recaptcha.verify():
            email = request.form.get('email')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')

            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists.', category='error')
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.', category='error')
            elif len(first_name) < 2:
                flash('First name must be greater than 1 characters.', category='error')
            elif len(last_name) < 2:
                flash('Last name must be greater than 1 characters.', category='error')
            elif password != confirm_password:
                flash('Password don\'t match.', category='eror')
            elif len(password) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(user, remember=True)
                flash('Account created!', category='success')
                return redirect(url_for('views.home'))

        else:
            flash('ReCaptcha required!', category='error')

    return render_template("sign_up.html", user=current_user)

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    first_name = current_user.first_name
    last_name = current_user.last_name
    if request.method == 'POST':
        if recaptcha.verify():
            user = User.query.filter_by(email=current_user.email).first()
            first_name = request.form.get('first_name')
            if first_name != '':
                user.first_name = first_name

            last_name = request.form.get('last_name')
            if last_name != '':
                user.last_name = last_name
            
            email = request.form.get('email')
            if email != '':
                user.email = email
                change = True
            else:
                change = False
   
            box = request.form.get('change_password')

            if box == 'on':
                old_password = request.form.get('old_password')
                new_password = request.form.get('new_password')
                new_password_confirm  = request.form.get('new_password_confirm')
                change_psw = False
                if old_password != '':
                    if new_password != '':
                        if new_password_confirm != '':
                            if old_password != new_password:
                                if new_password == new_password_confirm:
                                    if check_password_hash(current_user.password, old_password):
                                        user.password = generate_password_hash(new_password, method='sha256')
                                        change_psw = True
                                    else:
                                        flash('Incorrect old password!', category='error')
                            else:
                                flash('Password don\'t match.', category='eror')
                        else:
                            flash('Blank new password (confirm)!', category='error')
                    else:
                        flash('Blank new password!', category='error')
                else:
                    flash('Blank old password!', category='error')

            db.session.commit()
            
            if change == True:
                logout_user()
                flash("Account data changed successfully!", category='success')
                return redirect(url_for('auth.login'))
            if change_psw == True:
                flash('Password changed successfully!', category='succes')
                return redirect(url_for('auth.login'))
        else:
            flash('ReCaptcha required!', category='error')
    return render_template("profile.html", user=current_user)

