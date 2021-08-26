class funcionario():
    def __str__(self):
        return "This is an employee"
    def funcionarioDoMes(self):
        print("Congratz, you are the best employee in the month")
class alura(funcionario):
    def funcionarioDoMes(self):
        print("Congratz aluria,you are the best employee in the month")

class caelum(funcionario):
    def funcionarioDoMes(self):
        print("Congratz Caelium, you are the best employee in the month")

#MRO Method resolution order --> here we can see that the order of the methods rewritten are by the first father class methods
class junior(alura):
    pass
class pleno(caelum,alura):
    pass
class senior(alura,caelum):
    pass

senio = pleno()

senio.funcionarioDoMes()

