from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)

@app.route('/')
def home():
    return 'Привет мир!'

@app.route('/login_or_register', methods=['GET', 'POST'])
def login_or_register():
    if request.method == 'POST':
        action = request.form['action']
        return render_template('register_user.html' if action == 'register' else 'login.html')

    return render_template('login_or_register.html')

@app.route('/register_user', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone_mobile = request.form['phone_mobile']

    db = Database()
    # Проверка наличия пользователя в базе данных
    if db.user_exists(username):
        return 'User with this username already exists!'
    
    # Проверка наличия email и номера телефона в базе данных
    if db.email_exists(email) or db.phone_mobile_exists(phone_mobile):
        return 'Email or phone number is already registered!'

    db.insert_user(username, password, email, phone_mobile)
    db.close()

    return 'User Registration Successful!'

if __name__ == '__main__':
    app.run(debug=True)
