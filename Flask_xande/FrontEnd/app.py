from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from LibBiblioteca import ItemClass, AutorClass, UsuarioClass , PagamentoClass
from LibIntegracao import UsuarioNet , ItemNet
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from forms import LoginForm, RegistrationForm
from flask import request, session
from flask_session import Session

import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, password, email, confirmed=False):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.confirmed = confirmed

class UserLogin(UsuarioClass):

    def __init__(self, usuario, id):

        self.Nome = usuario.Nome
        self.Email = usuario.Email
        self.Senha = usuario.Senha
        self.Status = usuario.Status
        self.Assinatura = usuario.Assinatura
        self.is_active = True
        self.id = int(id)

    def get_id(self):
        return str(self.id)


@login_manager.user_loader
def load_user(id_usuario):
    Usuario = UsuarioNet()
    Usuario.obter(id_usuario)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        usuario_controler = UsuarioNet()
        index_forms = request.form.get('index')
        usuario = usuario_controler.obter(index_forms)
        print('a')
        print(usuario)

        if usuario.Senha == request.form.get("senha"):
            usuario_login = UserLogin(usuario, index_forms)
            print('d')
            login_user(usuario_login)
            session['usuario'] = usuario
            session["id"] = index_forms
            return redirect('/user_area')

    return render_template('login.html', usuarios = UsuarioNet().obterTodos())

@app.route('/user_area', methods=['GET', 'POST'])
def user_area():
    
    controle = UsuarioNet()
    delete = request.form.get("excluir")
    usuario = session.get('usuario')
    id = session.get('id')

    print(delete == True)

    if (delete == 'excluir'):
        logout_user()
        controle.excluir(id)
        return redirect('/login')
    else:
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        email = request.form.get("email")
        status = request.form.get("status")
        assinatura = True
        user = UsuarioClass(nome, email, senha, status, assinatura)
        controle.alterar(id,user)


    return render_template('user_area.html', usuario = usuario)


@app.route('/register', methods=['GET', 'POST'])
def register_teste():
    if request.method == 'POST':
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        email = request.form.get("email")
        status = request.form.get("status")
        assinatura = True
        a = UsuarioClass(nome, email, senha, status, assinatura)
        # print(a)
        Usuario = UsuarioNet()
        Usuario.incluir(p= a)
        return(redirect('/login'))
    return render_template("register.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


@app.route('/catalogo' ,  methods=['GET', 'POST'])
def catalogo():
    controle = ItemNet()
    livros = controle.obterTodos()
    print(livros)

    return render_template('catalogo.html' , livros = livros)

@app.route('/detalhamento/<chave>' ,  methods=['GET', 'POST'])
def detalhamento(chave):
    controle = ItemNet()
    livro = controle.obter(str(chave))
    print('a')
    print(livro.Autor)
    print(livro.Categoria)
    return render_template('detalhar.html' , livro = livro)

@app.route('/home' ,  methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/contato' ,  methods=['GET', 'POST'])
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
