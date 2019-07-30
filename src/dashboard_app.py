from flask import Flask, render_template, request, session, jsonify, send_file, Response, flash
from flask_bootstrap import Bootstrap
from wtforms import FloatField, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_wtf import Form, FlaskForm

app = Flask(__name__)
app.secret_key = "lucy"
Bootstrap(app)

#Search Form
class Search(FlaskForm):
    name = StringField('search', validators=[DataRequired()])


@app.route('/',methods= ["GET", "POST"])
def search():
    form = Search(request.form)
    search = ""

    if request.method == 'POST':
        search = request.form['search']
        if search.lower() == 'attain':
            return  render_template('dashboard- summary.html')
        else:
            return render_template('404.html')


    return render_template('login-register.html', form = form)

@app.route('/summary')
def start_dashboard():
    return render_template('dashboard- summary.html')


if __name__ == '__main__':
    app.run(port = "1208")