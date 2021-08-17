#teste evaluation acc = acc(1245,["Guilherme Cabrera","24/07/1996","Casado"],1994967,455,2000,3000)
"""
from bankAcc import acc
acc = acc(1245, ["Guilherme Cabrera","24/07/1996","Casado"], 1994967, 455, 2000, 3000)
"""

""""
1. Criar arquivo e script para verificar os dados para não cadastrar o user + de uma vez
    1.1. abrir arquivo
    1.2. for para ler linhas e comparar dados
    
2. Script para registrar, após validado
    2.1 adicionar registros em nova linha
    2.2 retornar msg de sucesso

3. Script Para acessar os dados caso já exista
    3.1 abrir arquivo
    3.2 for para ler dados do arquivo
    3.3 retornar dados
"""
class acc:
    #the atributes initializing with __ show us that they are atributes to be hadled only with methods
    def __init__(self,numberAcc,personalData,accPassword,eTokenGenNumber,saldo,limiteLins):
            self.__acc = numberAcc
            self.__saldo = saldo
            self.__limiteLins = limiteLins
            self.__personalData = personalData
            self.__accPassword = accPassword
            self.__eTokenGenNumber = eTokenGenNumber
    
    def checkUser(self):
        with open("myPass.json", "a") as myjson:
            for line in myjson:
                pass

    def extract(self):       
        print(f"Você possui: {self.__saldo}")
    def transaction(self,typeTransaction,valor):      
        
        if int((self.__limiteLins + self.__saldo) < int(valor)):
            print("Saldo insuficiente")
            quit()
        if typeTransaction == "withdraw":
            self.__saldo -= valor
            
        elif(typeTransaction == "deposit"):
            self.__saldo += valor
    @property
    def personalData(self):
        print(f"getter personalData {type(self.__personalData)}")
        return self.__personalData
    
    @personalData.setter
    def personalData(self, newPersonalData):
        if self.__checaList(newPersonalData,3):
            self.__personalData = newPersonalData
        else:
            print("Please tell us all the values needed")
    
    def __checaList(self, listVar, lenVar):
        return type(listVar) is list and len(listVar) == lenVar
            
    """
    Primeira forma de se criar métodos getters e setters
    def set_personalData():
        pass
    def set_accPassword():
        pass
    def set_accPassword():
        pass

    Segunda forma de se criar métodos getters e setters (a forma padrão)
    """
            




    
    
