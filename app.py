from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html', message="Hello World")


if __name__ == '__main__':
    app.run()
