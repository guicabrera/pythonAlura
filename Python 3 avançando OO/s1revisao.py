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
    ---------------------------------------------------------------------------------------------
    Sec 2 herança
"""

class programa:
    def __init__(self,nome,ano,categoria,funcionarios,likes):
        self.__nome = nome
        self.__ano = ano
        self.categoria = categoria
        self.funcionarios = funcionarios
        self.likes = 0
    
    @property
    def likes(self):
        return self.__likes
    @likes.setter
    def likes(self,likesToAdd):
        self.likes += int(likesToAdd)


class filmes(programa):
    def __init__(self,nomeFilme,anoFilme,categFilme,funcionariosFilme,duracaoFilme):
        if type(funcionariosFilme) is list:
            super().__init__(nomeFilme,anoFilme,categFilme,funcionariosFilme)
            self.__duracaoFilme = duracaoFilme            
        else:
            print("Please tell us the right information")
    @property
    def duracaoFilme(self):
        return self.__duracaoFilme
    @property
    def categFilme(self):
        return self.__categFilme.title()
    @property
    def anoFilme(self):
        return self.__anoFilme
    @property
    def nomeFilme(self):
        return self.__nomeFilme.title()
    @property
    def funcionariosFilme(self):
        return self.__funcionariosFilme       
    
    @funcionariosFilme.setter
    def funcionariosFilme(self,index,key,newValue):
        self.__funcionariosFilme[index][key] = newValue
"""
Dúvida --> como fazer o setter de uma propriedade tipo lista?

"""