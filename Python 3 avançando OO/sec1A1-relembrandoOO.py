class filmes():
    def __init__(self,nomeFilme,anoFilme,categFilme,funcionariosFilme,duracaoFilme):
        if type(funcionariosFilme) is dict:
            self.funcionariosFilme = funcionariosFilme
            self.nomeFilme = nomeFilme
            self.anoFilme = anoFilme
            self.categFilme = categFilme
            self.duracaoFilme = duracaoFilme
        else:
            pass