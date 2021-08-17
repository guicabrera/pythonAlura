class loja:
    
    def __init__(self, estoque, dadosLoja):
        if self.__verifyList(estoque) and self.__verifyList(dadosLoja):
            Self__estoque = estoque
            Self__dadosLoja = dadosLoja
        else:
            print("Please inform a correct value")
    def __verifyList(self, isList):
        return type(isList) is list