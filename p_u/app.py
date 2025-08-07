from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/academics')
def academics():
    return render_template('academics.html')

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/campus')
def campus():
    return render_template('campus.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Save to file / print for now (later: email or DB)
        print(f"New Contact - Name: {name}, Email: {email}, Message: {message}")
        flash('Your message has been sent!')
        return redirect('/contact')
    return render_template('contact.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        name = request.form['name']
        program = request.form['program']
        email = request.form['email']
        phone = request.form['phone']
        print(f"Application - {name}, {email}, {program}, {phone}")
        flash('Application submitted successfully!')
        return redirect('/apply')
    return render_template('apply.html')

if __name__ == '__main__':
    app.run(debug=True)
