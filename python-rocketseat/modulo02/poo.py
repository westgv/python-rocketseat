#POO

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    

pessoa1 = Pessoa("Gustavo", 30)

print(pessoa1.nome)
print(pessoa1.idade)
mensagem = pessoa1.saudacao()
print(mensagem)
