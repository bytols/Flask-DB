from flask import Flask
from flask import request, jsonify, make_response
from LibControllers import ItemController,AutorController, PagamentoController , UsuarioController
from LibBiblioteca import UsuarioClass, ItemClass, AutorClass, PagamentoClass

app = Flask(__name__)

controle_item = ItemController()
controle_user = UsuarioController()
controle_pagamento = PagamentoController()



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
    u = UsuarioClass(dados["Nome"], dados["Email"], dados["Senha"] , dados["Status"] , dados["Assinatura"] )
    controle_user.incluir(u)
    return jsonify(u.serialize())

@app.put("/api/usuario/<chave>")
def alterar(chave):
    dados = request.get_json()
    print(dados)
    u = controle_user.obter(chave)
    u.Nome = dados["Nome"]
    u.Email = dados["Email"]
    u.Senha = dados["Senha"]
    u.Status = dados["Status"]
    u.Assinatura = dados["Assinatura"]
    controle_user.alterar(u)
    return make_response("Alterado!",200)

@app.delete("/api/usuario/<chave>")
def excluir(chave):
    controle_user.excluir(chave)
    return make_response("Removido!",200)



# Catalogo

@app.get("/api/catalogo")
def obterTodosCatalogo():
    return jsonify(list(map(lambda x: x.serialize(), controle_item.obterTodos())))


@app.get("/api/catalogo/<chave>")
def obterCatalogo(chave):
    return jsonify(controle_item.obter(chave).serialize())

@app.post("/api/catalogo")
def incluirCatalogo():
    dados = request.get_json()
    u = ItemClass(dados["nome"], dados["idade"])
    u.chave = dados["chave"]
    controle_item.incluir(u)
    return jsonify(u.serialize())

@app.put("/api/catalogo/<chave>")
def alterarCatalogo(chave):
    dados = request.get_json()
    p = controle_item.obter(chave)
    p.nome = dados["nome"]
    p.idade = dados["idade"]
    controle_item.alterar(p)
    return make_response("Alterado!",200)

@app.delete("/api/catalogo/<chave>")
def excluirCatalogo(chave):
    controle_item.excluir(chave)
    return make_response("Removido!",200)




# pagamento




@app.get("/api/pagamento")
def obterTodosPagamento():
    return jsonify(list(map(lambda x: x.serialize(), controle_pagamento.obterTodos())))

@app.get("/api/pagamento/<chave>")
def obterPagamento(chave):
    return jsonify(controle_pagamento.obter(chave).serialize())

@app.post("/api/pagamento")
def incluirPagamento():
    dados = request.get_json()
    u = PagamentoClass(dados["Usuario"], dados["Valor_Pagamento"], dados["Metodo_Pagamento"] )
    controle_pagamento.incluir(u)
    return jsonify(u.serialize())

@app.put("/api/pagamento/<chave>")
def alterarPagamento(chave):
    dados = request.get_json()
    print(dados)
    u = controle_pagamento.obter(chave)
    u.Nome = dados["Nome"]
    u.Email = dados["Email"]
    u.Senha = dados["Senha"]
    u.Status = dados["Status"]
    u.Assinatura = dados["Assinatura"]
    controle_pagamento.alterar(u)
    return make_response("Alterado!",200)

@app.delete("/api/pagamento/<chave>")
def excluirPagamento(chave):
    controle_pagamento.excluir(chave)
    return make_response("Removido!",200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8001)