import requests
import json
from LibBiblioteca import ItemClass, AutorClass, UsuarioClass, PagamentoClass

def JSON2Item(dadosJSON):
    p = ItemClass(dadosJSON["Email"],dadosJSON["Nome"],dadosJSON["Senha"],dadosJSON["Status"],dadosJSON["id"])
    return p

def JSON2Pessoa(dadosJSON):
    p = UsuarioClass(dadosJSON["Email"],dadosJSON["Nome"],dadosJSON["Senha"],dadosJSON["Status"],dadosJSON["Assinatura"])
    return p

class UsuarioNet:
    def __init__(self):
        self.baseURL = 'http://127.0.0.1:8001/api/usuario'
        
    def obterTodos(self):
        resposta = requests.get(self.baseURL)
        return list(map(lambda x: JSON2Pessoa(x), json.loads(resposta.content)))
    
    def obter(self, matricula):
        resposta = requests.get(f'{self.baseURL}/{matricula}')
        return JSON2Pessoa(json.loads(resposta.content))
    
    def incluir(self, p):
        resposta = requests.post(self.baseURL,json=p.serialize())
        print(resposta)
        print(type(resposta))
        return JSON2Pessoa(json.loads(resposta.content))

    def alterar(self, p):
        resposta = requests.put(f'{self.baseURL}/{p.matricula}',json=p.serialize())
        return resposta.status_code # cod HTTP 200 = sucesso
    
    def excluir(self, matricula):
        resposta = requests.delete(f'{self.baseURL}/{matricula}')
        return resposta.status_code # cod HTTP 200 = sucesso