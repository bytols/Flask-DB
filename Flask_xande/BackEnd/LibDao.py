from LibBiblioteca import AutorClass , UsuarioClass , ItemClass , PagamentoClass
from SQL_Model import Autor , Usuario , Item , Pagamento
from SQL_Engine import engine
from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

class AutorDao:
    
    def __init__(self):
        pass

    def incluir(self, autor):
        session = Session()
        p = Autor(Nome_Autor = autor.Autor , Nacionalidade_Autor = autor.Nacionalidade)
        session.add(p)
        session.commit()
    def alterar(self, autor):
        session=Session()
        session.execute(update(Autor),[autor.serialize()])
        session.commit()
    def excluir(self, chave):
        session = Session()
        p = session.get(Autor, chave)
        print(p)
        session.delete(p)
        session.commit()
    def obterTodos(self):
        session = Session()
        stmt = select(Autor)
        autores = []
        for p in session.scalars(stmt):
            autor = AutorClass(p.Nome_Autor,p.Nacionalidade_Autor)
            autores.append(autor)
        session.commit()
        return autores
    def obter(self, chave):
        session = Session()
        p = session.get(Autor, chave)
        autor = AutorClass(p.Nome_Autor,p.Nacionalidade_Autor)
        session.commit()
        return autor

class UsuarioDao:

    def __init__(self):
        pass

    def incluir(self, usuario):
        session = Session()
        u = Usuario(Nome_Usuario = usuario.Nome , Email_Usuario = usuario.Email , Senha_Usuario =  usuario.Senha, Status_Usuario = usuario.Status , Assinatura = usuario.Assinatura )
        session.add(u)
        session.commit()
    def alterar(self, usuario):
        session=Session()
        session.execute(update(Usuario),[usuario.serialize()])
        session.commit()
    def excluir(self, chave):
        session = Session()
        u = session.get(Usuario, chave)
        print(u)
        session.delete(u)
        session.commit()
    def obterTodos(self):
        session = Session()
        stmt = select(Usuario)
        usuarios = []
        for u in session.scalars(stmt):
            usuario = UsuarioClass(u.Nome_Usuario , u.Email_Usuario , u.Senha_Usuario , u.Status_Usuario , u.Assinatura)
            usuarios.append(usuario)
        session.commit()
        return usuarios
    def obter(self, chave):
        session = Session()
        u = session.get(Usuario, chave)
        usuario = UsuarioClass(u.Nome_Usuario , u.Email_Usuario , u.Senha_Usuario , u.Status_Usuario , u.Assinatura)
        session.commit()
        return usuario

class ItemDao:

    def __init__(self):
        pass

    def incluir(self, item):
        session = Session()
        i = Item(Titulo_Item = item.Titulo , Descricao_Item = item.Descricao , Autor_Id =  item.Autor, Categoria_Id = item.Categoria, Id_Item = item.ID)
        session.add(i)
        session.commit()
    def alterar(self, item):
        session=Session()
        session.execute(update(Item),[item.serialize()])
        session.commit()
    def excluir(self, chave):
        session = Session()
        i = session.get(Item, chave)
        print(i)
        session.delete(i)
        session.commit()
    def obterTodos(self):
        session = Session()
        stmt = select(Item)
        items = []
        for u in session.scalars(stmt):
            item = ItemClass( u.Titulo_Item , u.Descricao_Item , u.Autor_Id , u.Categoria_Id, u.Id_Item )
            items.append(item)
        session.commit()
        return items
    def obter(self, chave):
        session = Session()
        u = session.get(Item, chave)
        item = ItemClass(u.Titulo_Item , u.Descricao_Item , u.Autor_Id , u.Categoria_Id, u.Id_Item)
        session.commit()
        return item
    

class PagamentoDao:

    def __init__(self):
        pass

    def incluir(self, pagamento):
        session = Session()
        p = Pagamento(Usuario_Id = pagamento.Usuario , Valor_Pagamento = pagamento.Valor_Pagamento , Metodo_Pagamento =  pagamento.Metodo_Pagamento)
        session.add(p)
        session.commit()
    def alterar(self, pagamento):
        session=Session()
        session.execute(update(Pagamento),[pagamento.serialize()])
        session.commit()
    def excluir(self, chave):
        session = Session()
        p = session.get(Pagamento, chave)
        print(p)
        session.delete(p)
        session.commit()
    def obterTodos(self):
        session = Session()
        stmt = select(Pagamento)
        pagamentos = []
        for p in session.scalars(stmt):
            pagamento = PagamentoClass(p.Usuario , p.Valor_Pagamento , p.Metodo_Pagamento  )
            pagamentos.append(pagamento)
        session.commit()
        return pagamentos
    def obter(self, chave):
        session = Session()
        p = session.get(Pagamento, chave)
        pagamento = PagamentoClass(p.Usuario , p.Valor_Pagamento , p.Metodo_Pagamento  )
        session.commit()
        return pagamento




