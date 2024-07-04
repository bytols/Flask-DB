from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from LibBiblioteca import ItemClass, AutorClass, UsuarioClass , PagamentoClass
from LibIntegracao import UsuarioNet
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'



# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gohan1603@gmail.com'
app.config['MAIL_PASSWORD'] = 'jxuf uctq goco uajr'

mail = Mail(app)
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, password, email, confirmed=False):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.confirmed = confirmed

# Usuário de exemplo (normalmente, você usaria um banco de dados)
users = [User(id=1, username='admin', password='password', email='admin@example.com', confirmed=True)]

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = next((u for u in users if u.username == username and u.password == password), None)
        if user:
            if not user.confirmed:
                flash('Please confirm your email address before logging in.', 'warning')
                return redirect(url_for('login'))
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form , usuarios = UsuarioNet().obterTodos())

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(id=len(users) + 1, username=form.username.data, password=form.password.data, email=form.email.data)
        users.append(new_user)

        # Geração do token de confirmação
        token = s.dumps(new_user.email, salt='email-confirm')

        # Construção do link de confirmação
        confirm_url = url_for('confirm_email', token=token, _external=True)

        # Construção do email de confirmação
        subject = "Please confirm your email"
        sender = 'seu_email@gmail.com'
        recipients = [new_user.email]
        body = f"Hi {new_user.username}, please click the link to confirm your email address: {confirm_url}"

        # Envio do email
        msg = Message(subject, sender=sender, recipients=recipients, body=body)
        mail.send(msg)

        flash('A confirmation email has been sent to you. Please check your inbox.', 'info')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        flash('The confirmation link has expired.', 'danger')
        return redirect(url_for('register'))
    
    user = next((u for u in users if u.email == email), None)
    if user:
        user.confirmed = True
        flash('Your account has been confirmed. Please log in.', 'success')
    else:
        flash('The confirmation link is invalid.', 'danger')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.username}! Welcome to your dashboard.'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
