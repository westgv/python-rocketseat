#Herança, Polimorfismo e Encapsulamento

# HERANÇA
print("\nExemplo Herança")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def andar(self):
        print(f'O animal {self.nome} andou')
        return
    
    def emitir_som(self):
        pass
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print(f"Cachorro se chama {dog.nome} e o Gato {cat.nome}")

animais = [dog,cat]

for animal in animais:
    print(f'{animal.nome} faz: {animal.emitir_som()}')

print("\nExemplo de encapsulamento")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(conta.consultar_saldo())
conta.depositar(valor=500)
print(conta.consultar_saldo())
conta.depositar(valor=-500)
print(conta.consultar_saldo())
conta.sacar(valor=200)
print(conta.consultar_saldo())

conta_do_zezinho = ContaBancaria(saldo=50)
print("\nExemplo de abstração: ")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):

    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    def desligar(self):
        return "Carro desligado utilizando a chave"

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())