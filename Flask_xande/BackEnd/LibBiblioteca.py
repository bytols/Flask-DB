class AutorClass:

    def __init__(self, Autor:str, Nacionalidade:str):
        
        self.Autor = Autor
        self.Nacionalidade = Nacionalidade

    def __repr__(self) -> str:
        return " é uma classe que gera um objeto Autor para o banco de dados, recebe os atributos, autor, nacionalidade e uma lista de item e retorna nada"
    
    def serialize(self):
        return {"Autor": self.Autor,
                "Nacionalidade": self.Nacionalidade,}