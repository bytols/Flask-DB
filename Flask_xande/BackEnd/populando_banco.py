from LibControllers import PagamentoController, AutorController, UsuarioController , ItemController
from SQL_Engine import engine
from sqlalchemy.orm import sessionmaker
from LibBiblioteca import AutorClass , ItemClass
from SQL_Model import Categoria, Autor



Session = sessionmaker(bind=engine)
Session = Session()


def cria_categoria():
    categoria_ficcao = Categoria(Nome_Categorias="ficcao", Descricao_Categoria="Livros que exploram histórias imaginárias e mundos fictícios.")
    categoria_suspense = Categoria(Nome_Categorias="suspense", Descricao_Categoria="Livros que mantêm o leitor em constante tensão e expectativa.")
    categoria_romance = Categoria(Nome_Categorias="romance", Descricao_Categoria="Livros que focam em relacionamentos amorosos e histórias emocionantes.")
    categoria_terror = Categoria(Nome_Categorias="terror", Descricao_Categoria="Livros que provocam medo e suspense, muitas vezes com elementos sobrenaturais.")
    categoria_aventura = Categoria(Nome_Categorias="aventura", Descricao_Categoria="Livros que envolvem ações emocionantes, explorações e jornadas épicas.")
    categoria_quadrinho = Categoria(Nome_Categorias="quadrinho", Descricao_Categoria="Livros em formato de quadrinhos, com narrativas visuais e texto.")
    categoria_infantil = Categoria(Nome_Categorias="infantil", Descricao_Categoria="Livros destinados ao público infantil, com histórias e ilustrações apropriadas para crianças.")
    categoria_academico = Categoria(Nome_Categorias="academico", Descricao_Categoria="Livros que abordam temas educacionais, científicos e de pesquisa.")

    Session.add(categoria_ficcao)
    Session.add(categoria_suspense)
    Session.add(categoria_romance)
    Session.add(categoria_terror)
    Session.add(categoria_aventura)
    Session.add(categoria_quadrinho)
    Session.add(categoria_infantil)
    Session.add(categoria_academico)

    Session.commit()

def criar_autores():
    controler = AutorController()

    # Autor 1: Stephen King
    Stephen_King = AutorClass(Autor="Stephen King", Nacionalidade="norte-americano")
    controler.incluir(Stephen_King)

    # Autor 2: J.K. Rowling
    JK_Rowling = AutorClass(Autor="J.K. Rowling", Nacionalidade="britânica")
    controler.incluir(JK_Rowling)

    # Autor 3: Gabriel Garcia Marquez
    Gabriel_Garcia_Marquez = AutorClass(Autor="Gabriel Garcia Marquez", Nacionalidade="colombiano")
    controler.incluir(Gabriel_Garcia_Marquez)

    # Autor 4: Agatha Christie
    Agatha_Christie = AutorClass(Autor="Agatha Christie", Nacionalidade="britânica")
    controler.incluir(Agatha_Christie)

    # Autor 5: George Orwell
    George_Orwell = AutorClass(Autor="George Orwell", Nacionalidade="britânico")
    controler.incluir(George_Orwell)

    # Autor 6: Haruki Murakami
    Haruki_Murakami = AutorClass(Autor="Haruki Murakami", Nacionalidade="japonês")
    controler.incluir(Haruki_Murakami)

    # Autor 7: J.R.R. Tolkien
    JRR_Tolkien = AutorClass(Autor="J.R.R. Tolkien", Nacionalidade="britânico")
    controler.incluir(JRR_Tolkien)

    # Autor 8: Isabel Allende
    Isabel_Allende = AutorClass(Autor="Isabel Allende", Nacionalidade="chilena")
    controler.incluir(Isabel_Allende)

    # Autor 9: Leo Tolstoy
    Leo_Tolstoy = AutorClass(Autor="Leo Tolstoy", Nacionalidade="russo")
    controler.incluir(Leo_Tolstoy)

    # Autor 10: Mark Twain
    Mark_Twain = AutorClass(Autor="Mark Twain", Nacionalidade="norte-americano")
    controler.incluir(Mark_Twain)

    Session.commit()

# Chamar a função para criar os autores

def incluir_items():

    categoria_ficcao = Session.query(Categoria).filter_by(Nome_Categorias = "ficcao" ).first()
    categoria_suspense = Session.query(Categoria).filter_by(Nome_Categorias = "suspense" ).first()
    categoria_romance = Session.query(Categoria).filter_by(Nome_Categorias = "romance" ).first()
    categoria_terror = Session.query(Categoria).filter_by(Nome_Categorias = "terror" ).first()
    categoria_aventura = Session.query(Categoria).filter_by(Nome_Categorias = "aventura" ).first()
    categoria_quadrinho = Session.query(Categoria).filter_by(Nome_Categorias = "quadrinho" ).first()
    categoria_infantil = Session.query(Categoria).filter_by(Nome_Categorias = "infantil" ).first()
    categoria_academico = Session.query(Categoria).filter_by(Nome_Categorias = "academico" ).first()


    Stephen_King = Session.query(Autor).filter_by(Nome_Autor = "Stephen King" ).first()
    JK_Rowling = Session.query(Autor).filter_by(Nome_Autor = "J.K. Rowling" ).first()
    Gabriel_Garcia_Marquez = Session.query(Autor).filter_by(Nome_Autor = "Gabriel Garcia Marquez" ).first()
    Agatha_Christie = Session.query(Autor).filter_by(Nome_Autor = "Agatha Christie" ).first()
    George_Orwell = Session.query(Autor).filter_by(Nome_Autor = "George Orwell" ).first()
    Haruki_Murakami = Session.query(Autor).filter_by(Nome_Autor = "Haruki Murakami" ).first()
    JRR_Tolkien = Session.query(Autor).filter_by(Nome_Autor = "J.R.R. Tolkien" ).first()
    Isabel_Allende = Session.query(Autor).filter_by(Nome_Autor = "Isabel Allende" ).first()
    Leo_Tolstoy = Session.query(Autor).filter_by(Nome_Autor = "Leo Tolstoy" ).first()
    Mark_Twain = Session.query(Autor).filter_by(Nome_Autor = "Mark Twain" ).first()
    Paulo_Coelho = Session.query(Autor).filter_by(Nome_Autor = "Paulo Coelho" ).first()

    controler =  ItemController()
    O_Alquimista = ItemClass(Titulo="O Alquimista", Descricao="A aventura de um pastor de ovelhas em busca de sua jornada pessoal e conhecendo os segredos do mundo e da alquimia", Autor=Paulo_Coelho.id_Autor, Categoria=categoria_aventura.Id_Categoria)
    controler.incluir(O_Alquimista)
    It = ItemClass(Titulo="It", Descricao="Um grupo de crianças enfrenta uma entidade maligna que assume a forma de um palhaço", Autor=Stephen_King.id_Autor, Categoria=categoria_terror.Id_Categoria)
    controler.incluir(It)
    a = ItemClass(Titulo="Harry Potter e a Pedra Filosofal", Descricao="A história de um jovem bruxo e suas aventuras na escola de magia", Autor=JK_Rowling.id_Autor, Categoria=categoria_ficcao.Id_Categoria)
    controler.incluir(a)
    b = ItemClass(Titulo="Cem Anos de Solidão", Descricao="A saga da família Buendía em uma aldeia fictícia na Colômbia", Autor=Gabriel_Garcia_Marquez.id_Autor, Categoria=categoria_romance.Id_Categoria)
    controler.incluir(b)
    c = ItemClass(Titulo="Assassinato no Expresso do Oriente", Descricao="Hercule Poirot investiga um assassinato a bordo de um trem de luxo", Autor=Agatha_Christie.id_Autor, Categoria=categoria_suspense.Id_Categoria)
    controler.incluir(c)
    d = ItemClass(Titulo="1984", Descricao="Uma distopia sobre um regime totalitário que controla todos os aspectos da vida", Autor=George_Orwell.id_Autor, Categoria=categoria_ficcao.Id_Categoria)
    controler.incluir(d)
    e = ItemClass(Titulo="Kafka à Beira-Mar", Descricao="A jornada surreal de um adolescente e um idoso em busca de verdades ocultas", Autor=Haruki_Murakami.id_Autor, Categoria=categoria_ficcao.Id_Categoria)
    controler.incluir(e)
    f = ItemClass(Titulo="O Senhor dos Anéis: A Sociedade do Anel", Descricao="Um grupo de heróis embarca em uma jornada épica para destruir um anel mágico", Autor=JRR_Tolkien.id_Autor, Categoria=categoria_aventura.Id_Categoria)
    controler.incluir(f)
    g = ItemClass(Titulo="A Casa dos Espíritos", Descricao="A vida de várias gerações de uma família chilena marcada por eventos sobrenaturais", Autor=Isabel_Allende.id_Autor, Categoria=categoria_romance.Id_Categoria)
    controler.incluir(g)
    h = ItemClass(Titulo="Guerra e Paz", Descricao="Um vasto panorama da sociedade russa durante as guerras napoleônicas", Autor=Leo_Tolstoy.id_Autor, Categoria=categoria_academico.Id_Categoria)
    controler.incluir(h)
    i = ItemClass(Titulo="As Aventuras de Tom Sawyer", Descricao="As peripécias de um garoto travesso nas margens do rio Mississippi", Autor=Mark_Twain.id_Autor, Categoria=categoria_infantil.Id_Categoria)
    controler.incluir(i)
    f = ItemClass(Titulo="Brida", Descricao="A história de uma jovem em busca de sabedoria espiritual", Autor=Paulo_Coelho.id_Autor, Categoria=categoria_romance.Id_Categoria)
    controler.incluir(f)
    g = ItemClass(Titulo="O Iluminado", Descricao="Um homem luta contra a possessão de um hotel assombrado", Autor=Stephen_King.id_Autor, Categoria=categoria_terror.Id_Categoria)
    controler.incluir(g)
    h = ItemClass(Titulo="Harry Potter e o Cálice de Fogo", Descricao="Harry compete em um torneio perigoso na escola de magia", Autor=JK_Rowling.id_Autor, Categoria=categoria_ficcao.Id_Categoria)
    controler.incluir(h)
    i = ItemClass(Titulo="Crônica de uma Morte Anunciada", Descricao="Uma narrativa sobre um assassinato em uma pequena cidade", Autor=Gabriel_Garcia_Marquez.id_Autor, Categoria=categoria_suspense.Id_Categoria)
    controler.incluir(i)
    j = ItemClass(Titulo="Morte no Nilo", Descricao="Poirot investiga um assassinato em um cruzeiro pelo Nilo", Autor=Agatha_Christie.id_Autor, Categoria=categoria_suspense.Id_Categoria)
    controler.incluir(j)
    k = ItemClass(Titulo="A Revolução dos Bichos", Descricao="Uma fábula política sobre uma revolução animal", Autor=George_Orwell.id_Autor, Categoria=categoria_ficcao.Id_Categoria)
    controler.incluir(k)
    l = ItemClass(Titulo="Norwegian Wood", Descricao="Uma história de amor e perda no Japão", Autor=Haruki_Murakami.id_Autor, Categoria=categoria_romance.Id_Categoria)
    controler.incluir(l)
    m = ItemClass(Titulo="O Hobbit", Descricao="Um hobbit embarca em uma aventura para ajudar os anões a recuperar seu lar", Autor=JRR_Tolkien.id_Autor, Categoria=categoria_aventura.Id_Categoria)
    controler.incluir(m)
    n = ItemClass(Titulo="Paula", Descricao="A autobiografia de Isabel Allende em forma de carta para sua filha", Autor=Isabel_Allende.id_Autor, Categoria=categoria_romance.Id_Categoria)
    controler.incluir(n)
    o = ItemClass(Titulo="Anna Karenina", Descricao="A trágica história de uma mulher russa e seu romance extraconjugal", Autor=Leo_Tolstoy.id_Autor, Categoria=categoria_romance.Id_Categoria)
    controler.incluir(o)
    p = ItemClass(Titulo="As Aventuras de Huckleberry Finn", Descricao="As aventuras de um jovem e um escravo fugitivo no rio Mississippi", Autor=Mark_Twain.id_Autor, Categoria=categoria_infantil.Id_Categoria)
    controler.incluir(p)
    q = ItemClass(Titulo="O Diário de um Mago", Descricao="A jornada espiritual de Paulo Coelho pelo caminho de Santiago", Autor=Paulo_Coelho.id_Autor, Categoria=categoria_academico.Id_Categoria)
    controler.incluir(q)



    Session.commit()






