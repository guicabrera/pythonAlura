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
    #special function that returns a message when we print the object programa
    def __str__(self):
        return f"Program information:\n Year: {self.ano}\n Name: {self.ano}\n Category: {self.categoria}\nLikes: {self.likes}\n"
    
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
    def darLike(self):
        self.likes = 1
class filmes(programa):
    def __init__(self,nomeFilme,anoFilme,categFilme,funcionariosFilme,duracaoFilme):
            super().__init__(nomeFilme,anoFilme,categFilme,funcionariosFilme)
            self.__duracaoFilme = duracaoFilme
    def __str__(self):
        return f"Program information:\n Year: {self.ano}\n Name: {self.ano}\n Category: {self.categoria}\n Likes: {self.likes}\n Duration: {self.duracaoFilme}\n"
    @property
    def duracaoFilme(self):
        return self.__duracaoFilme
class serie(programa):
    def __init__(self,nomeSerie,anoSerie,categSerie,funcionariosSerie,temporadasSerie,duracaoEpisodio):
        super().__init__(nomeSerie,anoSerie,categSerie,funcionariosSerie)
        self.__temporadasSerie = temporadasSerie
        self.__duracaoEpisodio = duracaoEpisodio
    def __str__(self):
        return f"Program information:\n Year: {self.ano}\n Name: {self.ano}\n Category: {self.categoria}\n Likes: {self.likes}\n Duration: {self.duracaoEpisodio}\n Seasons: {self.temporadasSerie}\n"
    @property
    def temporadasSerie(self):
        return self.__temporadasSerie
    @property
    def duracaoEpisodio(self):
        return self.__duracaoEpisodio

class playList(list):
    def __init__(self, playlistName,listaProgramas) :
        self.__name = playlistName
        super().__init__(listaProgramas)





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
hp1.darLike()
hp1.darLike()
hp1.darLike()
hp1.darLike()
himym = serie("How I Meet Your Mother","2005","Humor",funcionarios,10,25)
himym.darLike()
himym.darLike()
himym.darLike()
himym.darLike()
myPrograms = [hp1,himym]

minhaPlayList = playList("Nerd List",[hp1,himym])
for item in minhaPlayList:
    print(item)
