# including the flask library/module
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

# making an instance 'app' of Flask class
app = Flask(__name__)

# email configurations
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'write your email'
app.config['MAIL_PASSWORD'] = 'write your password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# this line of code connects our flask application with the smpt gmail server.
mail = Mail(app) 

# creating route to handle request
@app.route('/')
def home():
    return render_template('index.html')

# creating a route to handle about us
@app.route('/about')
def about():
    return "This is about page of the matrimonial site"

# creating a submit route
@app.route('/submit', methods = ['POST'])
def submit():
    
    # extracting the data from the request
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    phone = request.form.get('user_phone')
    dob = request.form.get('user_dob')
    hobbies = request.form.get('user_hobbies')
    print(name, email, phone, dob, hobbies)

    # send the email to the user
    msg1 = Message( 
                'Shaadi.com: Confirmation for bio data submission', 
                sender ='Write your email', 
                recipients = [email] 
               ) 
    msg1.body = 'Thank you for submitting the bio data. We will find your match and connect with you shortly.'

    msg2 = Message( 
                'Shaadi.com: Another query from a customer', 
                sender ='Write your email', 
                recipients = ['Write your admin email'] 
               ) 
    msg2.body = f'{name}\n{email}\n{phone}\n{dob}\n{hobbies}'

    mail.send(msg1)
    mail.send(msg2)



    return redirect('/')
    


# let's run the server/app
app.run(debug=True)

