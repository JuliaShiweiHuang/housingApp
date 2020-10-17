from flask import Flask, render_template
from data import Resources
app = Flask(__name__)

Resources = Resources()

@app.route('/')# add app route
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/resources')
def resources():
    return render_template('resources.html', resources = Resources)    


@app.route('/resource/<string:id>')
def resource(id):
    return render_template('resource.html', id=id)    

if __name__ == '__main__':
    app.run(debug = True)
