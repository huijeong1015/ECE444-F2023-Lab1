from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

def check_uoft_email(form, field):
    if not 'utoronto' in field.data:
        raise ValidationError('Enter U of T email address.')

class Forms(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your U of T email address?', validators=[DataRequired(), check_uoft_email])
    submit = SubmitField('Submit')
    
@app.route('/', methods=['GET', 'POST'])
def index():
    forms = Forms()
    if forms.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != forms.name.data:
            flash('Looks like you have changed your name!')
            print("Flash message")
        session['name'] = forms.name.data
        session['email'] = forms.email.data
        return redirect(url_for('index'))
    return render_template('index.html', forms=forms, name=session.get('name'), email=session.get('email'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
