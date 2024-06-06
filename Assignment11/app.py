import os
from flask import Flask, render_template, send_file
app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route('/resume_download')
def resume_download():
    path = os.path.join('pdf', 'BenyaminZojaji-resume2024.pdf')
    return send_file(path)


if __name__ == '__main__':
    app.run(debug=True)
