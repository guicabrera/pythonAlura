class Parent:
  def __init__(self, txt):
      self.message = txt
    

  def printmessage(self):
      print(self.message)

class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)
    def printmessage(self):
        print("trying super method")
        super().printmessage()
    
    @classmethod
    def teste(cls):
        pass
    

x = Child("Hello, and welcome!")

x.printmessage()
