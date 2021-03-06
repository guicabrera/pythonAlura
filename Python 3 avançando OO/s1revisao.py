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
    def __init__(self,nome,ano,categoria,funcionarios):
        if type(funcionarios) is list:
            self.__nome = nome
            self.__ano = ano
            self.__categoria = categoria
            self.__funcionarios = funcionarios
            self.__likes = 0
        else:
            print("Please tell us the right information")
            quit()
    
    @property
    def nome(self):
        return self.__nome
    @property
    def ano(self):
        return self.__ano
    @property
    def categoria(self):
        return self.__categoria
    @property
    def funcionarios(self):
        return self.__funcionarios
    @property
    def likes(self):
        return self.__likes
    @likes.setter
    def likes(self,likesToAdd):
        self.__likes += int(likesToAdd)
    @funcionarios.setter
    def funcionarios(self,newFuncionario):
        self.__funcionarios.append(newFuncionario)

    def alteraFuncionario(self,index,key,newValue):
        self.__funcionarios[index][key] = newValue

class filmes(programa):
    def __init__(self,nomeFilme,anoFilme,categFilme,funcionariosFilme,duracaoFilme):
            super().__init__(nomeFilme,anoFilme,categFilme,funcionariosFilme)
            self.__duracaoFilme = duracaoFilme

class serie(programa):
    def __init__(self,nomeSerie,anoSerie,categSerie,funcionariosSerie,temporadasSerie,duracaoEpisodio):
        super().__init__(nomeSerie,anoSerie,categSerie,funcionariosSerie)
        self.__temporadasSerie = temporadasSerie
        self.__duracaoEpisodio = duracaoEpisodio
    
    @property
    def temporadasSerie(self):
        return self.__temporadasSerie
    @property
    def duracaoEpisodio(self):
        return self.__duracaoEpisodio
        
    """       
    @funcionariosFilme.setter
    def funcionariosFilme(self,index,key,newValue):
        self.__funcionariosFilme[index][key] = newValue"""
"""
Dúvida --> como fazer o setter de uma propriedade tipo lista?

"""