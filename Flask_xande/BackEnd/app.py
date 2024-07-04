from flask import Flask
from flask import request, jsonify, make_response
from LibControllers import ItemController,AutorController, PagamentoController , UsuarioController
from LibBiblioteca import UsuarioClass, ItemClass, AutorClass, PagamentoClass

app = Flask(__name__)

controle_item = ItemController()
controle_user = UsuarioController()



# lista = [1,2,3,4,5]
#def multiplica(x:int):
#    return x*2
#print(map(lambda x: x.2 , lista))
# map(multiplica() , lista)


@app.get("/api/usuario")
def obterTodos():
    return jsonify(list(map(lambda x: x.serialize(), controle_user.obterTodos())))

@app.get("/api/usuario/<chave>")
def obter(chave):
    return jsonify(controle_user.obter(chave).serialize())

@app.post("/api/usuario")
def incluir():
    dados = request.get_json()
    u = UsuarioClass(dados["nome"], dados["idade"])
    u.matricula = dados["matricula"]
    controle_user.incluir(u)
    return jsonify(u.serialize())

@app.put("/api/usuario/<matricula>")
def alterar(matricula):
    dados = request.get_json()
    p = controle_user.obter(matricula)
    p.nome = dados["nome"]
    p.idade = dados["idade"]
    controle_user.alterar(p)
    return make_response("Alterado!",200)

@app.delete("/api/usuario/<matricula>")
def excluir(matricula):
    controle_user.excluir(matricula)
    return make_response("Removido!",200)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8001)



# Catalogo

@app.get("/api/catalogo")
def obterTodos():
    return jsonify(list(map(lambda x: x.serialize(), controle_item.obterTodos())))


@app.get("/api/catalogo/<chave>")
def obter(chave):
    return jsonify(controle_item.obter(chave).serialize())

@app.post("/api/catalogo")
def incluir():
    dados = request.get_json()
    u = ItemClass(dados["nome"], dados["idade"])
    u.matricula = dados["matricula"]
    controle_item.incluir(u)
    return jsonify(u.serialize())

@app.put("/api/catalogo/<matricula>")
def alterar(matricula):
    dados = request.get_json()
    p = controle_item.obter(matricula)
    p.nome = dados["nome"]
    p.idade = dados["idade"]
    controle_item.alterar(p)
    return make_response("Alterado!",200)

@app.delete("/api/catalogo/<matricula>")
def excluir(matricula):
    controle_item.excluir(matricula)
    return make_response("Removido!",200)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8001)