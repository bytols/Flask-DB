from LibBiblioteca import AutorClass
from LibDao import AutorDao

class AutorController:
    def __init__(self):
        self.dao = AutorDao()
    def incluir(self, autor):
        if(type(autor) is not AutorClass):
            raise "Não é uma pessoa!"
        return self.dao.incluir(autor)
    def alterar(self, autor):
        self.dao.alterar(autor)
    def excluir(self, chave):
        self.dao.excluir(chave)
    def obterTodos(self):
        return list(self.dao.obterTodos())
    def obter(self, chave):
        return self.dao.obter(chave)
    
if __name__ == '__main__':
    controle = AutorController()
    p1 = AutorClass("Stephen King","norte-americano")
    print(controle.incluir(p1))
    # p2 = AutorClass("Paulo Coelho","Brasileiro")
    # print(controle.incluir(p2))
    # for p in controle.obterTodos():
    #     print(p)