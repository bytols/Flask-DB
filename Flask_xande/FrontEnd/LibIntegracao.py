import requests
import json
from LibBiblioteca import ItemClass, AutorClass, UsuarioClass, PagamentoClass

def JSON2Item(dadosJSON):
    p = ItemClass(dadosJSON["Autor"],dadosJSON["Categoria"],dadosJSON["Descricao"],dadosJSON["Titulo"])
    return p

def JSON2Pessoa(dadosJSON):
    p = UsuarioClass(dadosJSON["Email"],dadosJSON["Nome"],dadosJSON["Senha"],dadosJSON["Status"],dadosJSON["Assinatura"])
    return p

def JSON2Pagamento(dadosJSON):
    p = UsuarioClass(dadosJSON["Usuario"],dadosJSON["Valor_Pagamento"],dadosJSON["Metodo_Pagamento"])
    return p

class UsuarioNet:
    def __init__(self):
        self.baseURL = 'http://127.0.0.1:8001/api/usuario'

    def obterTodos(self):
        resposta = requests.get(self.baseURL)
        return list(map(lambda x: JSON2Pessoa(x), json.loads(resposta.content)))
    
    def obter(self, chave):
        resposta = requests.get(f'{self.baseURL}/{str(chave)}')
        return JSON2Pessoa(json.loads(resposta.content))
    
    def incluir(self, p):
        resposta = requests.post(self.baseURL,json=p.serialize())
        
    def alterar(self, chave , user):
        resposta = requests.put(f'{self.baseURL}/{chave}',json=user.serialize())
        return resposta.status_code # cod HTTP 200 = sucesso
    
    def excluir(self, chave):
        resposta = requests.delete(f'{self.baseURL}/{chave}')
        return resposta.status_code # cod HTTP 200 = sucesso
    
class ItemNet:
    def __init__(self):
        self.baseURL = 'http://127.0.0.1:8001/api/catalogo'
        
    def obterTodos(self):
        resposta = requests.get(self.baseURL)
        return list(map(lambda x: JSON2Item(x), json.loads(resposta.content)))
    
    def obter(self, chave):
        print(chave)
        resposta = requests.get(f'{self.baseURL}/{str(chave)}')
        return JSON2Item(json.loads(resposta.content))
    
    def incluir(self, p):
        print(p)
        resposta = requests.post(self.baseURL,json=p.serialize())
        
    def alterar(self, chave , user):
        resposta = requests.put(f'{self.baseURL}/{chave}',json=user.serialize())
        return resposta.status_code # cod HTTP 200 = sucesso
    
    def excluir(self, chave):
        resposta = requests.delete(f'{self.baseURL}/{chave}')
        return resposta.status_code # cod HTTP 200 = sucesso
    
class PagamentoNet:
    def __init__(self):
        self.baseURL = 'http://127.0.0.1:8001/api/pagamento'
        
    def obterTodos(self):
        resposta = requests.get(self.baseURL)
        return list(map(lambda x: JSON2Pagamento(x), json.loads(resposta.content)))
    
    def obter(self, chave):
        print(chave)
        resposta = requests.get(f'{self.baseURL}/{str(chave)}')
        return JSON2Pagamento(json.loads(resposta.content))
    
    def incluir(self, p):
        print(p)
        resposta = requests.post(self.baseURL,json=p.serialize())
        print(resposta)
        
    def alterar(self, chave , user):
        resposta = requests.put(f'{self.baseURL}/{chave}',json=user.serialize())
        return resposta.status_code # cod HTTP 200 = sucesso
    
    def excluir(self, chave):
        resposta = requests.delete(f'{self.baseURL}/{chave}')
        return resposta.status_code # cod HTTP 200 = sucesso