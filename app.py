from flask import Flask, render_template, jsonify, request


import requests

app = Flask(__name__, static_folder='static')
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


