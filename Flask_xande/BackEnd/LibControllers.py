from LibBiblioteca import AutorClass, ItemClass, UsuarioClass, PagamentoClass
from LibDao import AutorDao , ItemDao , UsuarioDao , PagamentoDao
from sqlalchemy.orm import sessionmaker
from SQL_Engine import engine
from SQL_Model import Autor
from sqlalchemy import event , text


class AutorController:
    def __init__(self):
        self.dao = AutorDao()
    def incluir(self, autor):
        if(type(autor) is not AutorClass):
            raise "Não é um autor!"
        return self.dao.incluir(autor)
    def alterar(self, autor):
        self.dao.alterar(autor)
    def excluir(self, chave):
        self.dao.excluir(chave)
    def obterTodos(self):
        return list(self.dao.obterTodos())
    def obter(self, chave):
        return self.dao.obter(chave)
    
class UsuarioController:
    def __init__(self):
        self.dao = UsuarioDao()
    def incluir(self, usuario):
        if(type(usuario) is not UsuarioClass):
            raise "Não é um Usuario Cadastrado!"
        return self.dao.incluir(usuario)
    def alterar(self, usuario):
        self.dao.alterar(usuario)
    def excluir(self, chave):
        self.dao.excluir(chave)
    def obterTodos(self):
        return list(self.dao.obterTodos())
    def obter(self, chave):
        return self.dao.obter(chave)
    
class ItemController:
    def __init__(self):
        self.dao = ItemDao()
    def incluir(self, item):
        if(type(item) is not ItemClass):
            raise "Não é um Item Cadastrado!"
        return self.dao.incluir(item)
    def alterar(self, item):
        self.dao.alterar(item)
    def excluir(self, chave):
        self.dao.excluir(chave)
    def obterTodos(self):
        return list(self.dao.obterTodos())
    def obter(self, chave):
        return self.dao.obter(chave)
    
class PagamentoController:
    def __init__(self):
        self.dao = PagamentoDao()
    def incluir(self, pagamento):
        if(type(pagamento) is not PagamentoClass):
            raise "Não é um pagamento Cadastrado!"
        return self.dao.incluir(pagamento)
    def alterar(self, pagamento):
        self.dao.alterar(pagamento)
    def excluir(self, chave):
        self.dao.excluir(chave)
    def obterTodos(self):
        return list(self.dao.obterTodos())
    def obter(self, chave):
        return self.dao.obter(chave)
        
if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    Session = Session()

    # controle = AutorController()
    # p1 = AutorClass("Stephen King","norte-americano")
    # print(controle.incluir(p1))
    # p2 = AutorClass("Paulo Coelho","Brasileiro")
    # print(controle.incluir(p2))
    # for p in controle.obterTodos():
    #     print(p)

    # p = controle.obter(1)
    # p.id_autor = 1
    
    # print(p)

    # p.Nacionalidade = "Brasileiro"

    # controle.alterar(p)

    # p =Session.get(Autor,1)
    # autor_a_excluir = Session.query(Autor).filter_by(id_Autor=1).first()
    # Session.delete(autor_a_excluir)
    # Session.commit()

