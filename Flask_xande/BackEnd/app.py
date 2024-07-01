from flask import Flask
from flask import request, jsonify, make_response
from LibControllers import ItemController,AutorController, PagamentoController , UsuarioController
from LibBiblioteca import UsuarioClass, ItemClass, AutorClass, PagamentoClass

app = Flask(__name__)

controle = UsuarioController()

@app.get("/api/usuario")
def obterTodos():
    return jsonify(list(map(lambda x: x.serialize(), controle.obterTodos())))

@app.get("/api/usuario/<matricula>")
def obter(matricula):
    return jsonify(controle.obter(matricula).serialize())

@app.post("/api/usuario")
def incluir():
    dados = request.get_json()
    u = UsuarioClass(dados["nome"], dados["idade"])
    u.matricula = dados["matricula"]
    controle.incluir(u)
    return jsonify(u.serialize())

@app.put("/api/usuario/<matricula>")
def alterar(matricula):
    dados = request.get_json()
    p = controle.obter(matricula)
    p.nome = dados["nome"]
    p.idade = dados["idade"]
    controle.alterar(p)
    return make_response("Alterado!",200)

@app.delete("/api/usuario/<matricula>")
def excluir(matricula):
    controle.excluir(matricula)
    return make_response("Removido!",200)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8001)