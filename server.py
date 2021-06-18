from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def box():
    return render_template('index.html')

@app.route('/play')
def three_box():
    return render_template('three.html', count = 3, color = 'aqua')

@app.route('/play/<count>')
def multi_box(count):
    return render_template('three.html', count = int(count), color = 'aqua')

@app.route('/play/<count>/<color>')
def coloring(count, color):
    return render_template('three.html', count = int(count), color = color)


if __name__ == '__main__':
    app.run(debug = True)