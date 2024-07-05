class AutorClass:

    def __init__(self, Autor:str, Nacionalidade:str):
        
        self.id_Autor = 1
        self.Autor = Autor
        self.Nacionalidade = Nacionalidade

    def __str__(self):
        return f""" id:{self.id_Autor} Autor:{self.Autor} , Nacionalidade:{self.Nacionalidade} """ 

    def __repr__(self) -> str:
        return f" é uma classe que gera um objeto Autor para o banco de dados, recebe os atributos, autor, nacionalidade, Autor:{self.Autor} , Nacionalidade:{self.Nacionalidade} "
    
    def serialize(self):
        return {"Autor": self.Autor,
                "Nacionalidade_Autor": self.Nacionalidade,
                "id_Autor": self.id_Autor}
    

class UsuarioClass:

    def __init__(self, Nome:str , Email:str , Senha:str , Status:str , Assinatura:bool ):
        self.Nome = Nome
        self.Email = Email
        self.Senha = Senha
        self.Status = Status
        self.Assinatura = Assinatura

    def __str__(self):
        return  f"""Nome:{self.Nome} , Email:{self.Email} , Senha:{self.Senha} , Status:{self.Status} ,Assinatura:{self.Assinatura} """ 

    def __repr__(self) -> str:
        return f""" é uma classe que gera um objeto Usuario para o banco de dados, recebe os atributos, nome, email, senha, status e situação da assinatura
                Nome:{self.Nome} , Email:{self.Email} , Senha:{self.Senha} , Status:{self.Status} ,Assinatura:{self.Assinatura}
        """
    
    def serialize(self):
        return {"Nome": self.Nome,
                "Email": self.Email,
                "Senha" : self.Senha,
                "Status" : self.Status,
                "Assinatura" : self.Assinatura}
    
        
class ItemClass:

    def __init__(self ,Titulo:str , Descricao:str , Autor: object , Categoria: object):
        self.Titulo = Titulo
        self.Descricao = Descricao
        self.Autor = Autor
        self.Categoria = Categoria
    
    def __repr__(self) -> str:
        return f"""  Titulo:{self.Titulo} , Autor:{self.Autor} , Descricao:{self.Descricao} , Categoria:{self.Categoria} """

    def __repr__(self) -> str:
        return f""" é uma classe que gera um objeto Livro para o banco de dados, recebe os atributos, nome, email, senha, status e situação da assinatura
                Titulo:{self.Titulo} , Autor:{self.Autor} , Descricao:{self.Descricao} , Categoria:{self.Categoria}
        """
    
    def serialize(self):
        return {"Titulo": self.Titulo,
                "Descricao": self.Descricao,
                "Autor" : self.Autor,
                "Categoria" : self.Categoria}
    
class PagamentoClass:

    def __init__(self , Usuario:object , Valor_Pagamento:int , Metodo_Pagamento:str ):
        self.Usuario = Usuario
        self.Valor_Pagamento = Valor_Pagamento
        self.Metodo_Pagamento = Metodo_Pagamento

    def __repr__(self) -> str:
        return f""" Nome:{self.Usuario} , Email:{self.Valor_Pagamento} , Senha:{self.Metodo_Pagamento} """

    def __repr__(self) -> str:
        return f""" é uma classe que gera um objeto Livro para o banco de dados, recebe os atributos, nome, email, senha, status e situação da assinatura
                Nome:{self.Usuario} , Email:{self.Valor_Pagamento} , Senha:{self.Metodo_Pagamento}
        """
    
    def serialize(self):
        return {"Usuario": self.Usuario,
                "Valor_Pagamento": self.Valor_Pagamento,
                "Metodo_Pagamento" : self.Metodo_Pagamento}