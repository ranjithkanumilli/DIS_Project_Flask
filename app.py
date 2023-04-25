from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

import requests

app = Flask(__name__, static_folder='static')
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "thisisasecretkey"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    IMG_URL = 'https://image.tmdb.org/t/p/w500'
    IMG_URL_ORIGINAL = 'https://image.tmdb.org/t/p/original'

    # The API endpoint to fetch movies from
    BASE_URL = 'https://api.themoviedb.org/3'
    # The API key needed to authenticate the request
    api_key = 'f55104d0cb044a5ac6b66815a2732922'
    TRENDING_MOVIES_URL = BASE_URL + '/trending/movie/week?'
    TRENDING_TV_URL = BASE_URL + '/trending/tv/week?'
    # The query parameters to include in the request
    params = {
        'api_key': api_key
    }
    # Make the API request and get the JSON response
    response = requests.get(TRENDING_MOVIES_URL, params=params)
    trendingmovies = response.json()

    response = requests.get(TRENDING_TV_URL, params=params)
    trendingtv = response.json()

    return render_template('index.html', movies=trendingmovies['results'], tv=trendingtv['results'], IMG_URL=IMG_URL, title='My Website', IMG_URL_ORIGINAL=IMG_URL_ORIGINAL)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/movies')
def movies():
    return render_template('moviesPage.html')


@app.route('/tvshows')
def tvshows():
    return render_template('TvShowsPage.html')


@app.route('/product')
def product():
    id = request.args.get('id')
    product_type = request.args.get('type')
    return render_template('Product.html', id=id, type=product_type)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/chart')
def chart():
    return render_template('chart.html')


if __name__ == '__main__':
    app.run(debug=True)
