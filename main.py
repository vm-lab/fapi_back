from flask import Flask, render_template
from content import payload

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', payload=payload)


@app.route('/about')
def about():
    return render_template('about.html')


if (__name__) == ('__main__'):
    app.run(debug=True)
