from flask import Flask, render_template, request



app = Flask(__name__, static_folder='static')
@app.route('/')
def home():
    return render_template('index.html', title='My Website')

@app.route('/movies')
def movies():
    return render_template('moviesPage.html')

@app.route('/tvshows')
def tvshows():
    return render_template('TvShowsPage.html')

@app.route('/product')
def product():
    return render_template('Product.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')


if __name__ == '__main__':
    app.run(debug=True)

