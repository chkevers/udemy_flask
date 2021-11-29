from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/home')
def welcome():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/albums')
def album_page():
    return render_template('albums.html')

@app.route('/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['bipuser'] == 'chkevers' and request.form['bippw'] == 'admin':
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials. Please try again'
            return render_template('login.html', error=error)
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)