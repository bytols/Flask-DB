from LibBiblioteca import AutorClass
from SQL_Model import Autor
from SQL_Engine import engine
from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

class AutorDao:
    
    def __init__(self):
        pass

    def incluir(self, autor):
        session = Session()
        p = Autor(Nome_Autor = autor.Autor , Nacionalidade_Autor = autor.Nacionalidade,  id_Autor = 4)
        session.add(p)
        session.commit()
        


# autor = Autor(Nome_Autor = "Stephen King", Nacionalidade_Autor = "norte-americano" , id_Autor = 1)

# Session.add(autor)
# Session.commit()
