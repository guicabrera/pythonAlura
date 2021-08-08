#to help us test the script:
"""
from s1revisao import filmes
    funcionarios = [
        {   
            "nome":"Alisson",
            "idade":25,
            "salario":5000,
            "funcao":"Atriz",
            "idFuncionario":35478
        },
        {
            "nome":"Jonas",
            "idade":30,
            "salario":15000,
            "funcao":"Diretor",
            "idFuncionario":20555
        },
        {
            "nome":"Fernan",
            "idade":25,
            "salario":5000,
            "funcao":"Ator",
            "idFuncionario":35479
        }
    ]
    hp1 = filmes("Harry Potter e a Pedra filosofal",1999,"Ficção mística",funcionarios,220)
"""
class filmes():
    def __init__(self,nomeFilme,anoFilme,categFilme,funcionariosFilme,duracaoFilme):
        if type(funcionariosFilme) is list:
            self.__funcionariosFilme = funcionariosFilme
            self.__nomeFilme = nomeFilme.title()
            self.__anoFilme = anoFilme
            self.__categFilme = categFilme.title()
            self.__duracaoFilme = duracaoFilme
            self.__likes = 0
        else:
            print("Please tell us the right information")

    @property
    def likes(self):
        return self.__likes
    @likes.setter
    def likes(self,likesToAdd):
        self.likes += int(likesToAdd)