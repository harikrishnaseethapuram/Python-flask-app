from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/placements')
def placements():
    return render_template('placements.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)