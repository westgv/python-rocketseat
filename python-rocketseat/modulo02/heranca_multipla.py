class Animal:
    def __init__(self) -> None:
        self.nome = nome
        
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} esta voando."
    
class Morcego(Mamifero, Ave):

    #super chama a implementação da classe mãe.

    def emitir_som(self):
        return "Morcegos emitem sons ultrasônicos"
    
    def voar(self):
        return super().voar()