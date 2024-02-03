from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
from user import User 

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']  # Consider hashing this password before storing
        registration_date = datetime.datetime.now()
        # Create an instance of User and register
        user = User()
        user.create_database()
        
        user.create_table()
        user.insert_user(name, email, phone, password, registration_date)
        rows=user.fetch_data()
        for row in rows:
            print(row)
        return 'SignednUP'  # Redirect to a success page or another route as desired
    return render_template('signup.html')


@app.route('/dashboard') 
def dashboard():
    return render_template('dashboard.html')

@app.route('/login',methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if password is not None and name is not None:

            details=User.search(name,password)
            print(details)
            if(details):
                flag=True
                # return redirect('/dashboard.html')
                return redirect(url_for('dashboard.html'))
                
            else:
                flag=False
                return "UnAuthorized"
        
    else:
        return render_template('login.html')
    
@app.route('/documentation') 
def documentation():
    return render_template('documentation.html')

if __name__ == '__main__':
    app.run(debug=True)

    