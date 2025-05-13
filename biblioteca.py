class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.dormindo = False
        self.falando = False
        self.comendo = False

    def falar(self):
        if self.falando == True:
            print("não pode falar, pois, já está falando")

        print(f" {self.nome} começou a falar ")

    def comer(self, comida):
        if self.comendo == True:
            print("não pode comer, pois, já está comendo")

        print(f" foi comer {comida}")

    def dormir(self):
        if self.dormindo == True:
            print("Foi doemir... Zzz")
        elif self.falando == True:
            print("não pode dormir, pois, está falando.")
        elif self.comendo == True:
            print("não pode dormir, pois, está comendo.")
        else:
            print("Foi dormir")
            self.dormindo = True

    def acordar(self):
        if self.dormindo == True:
            self.dormindo = False
            print("Acordou o mizeravel")
        else:
            print()

class ContaBancaria:
    def __init__(self, numero_conta, nome_cliente):
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.saldo = 0.0
        self.ativa = False

    def depositar(self, valor):
        if self.ativa:
            if valor > 0:
                self.saldo += valor
                print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            else:
                print("Valor de depósito deve ser positivo.")
        else:
            print("Conta inativa. Não é possível realizar depósito.")

    def sacar(self, valor):
        if self.ativa:
            if 0 < valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente ou valor inválido.")
        else:
            print("Conta inativa. Não é possível realizar saque.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
        return self.saldo

    def ativar_conta(self):
        if not self.ativa:
            self.ativa = True
            print("Conta ativada com sucesso.")
        else:
            print("A conta já está ativa.")

    def desativar_conta(self):
        if self.ativa:
            if self.saldo == 0:
                self.ativa = False
                print("Conta desativada com sucesso.")
            else:
                print("Não é possível desativar a conta com saldo diferente de zero.")
        else:
            print("A conta já está inativa.")

class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"O {self.nome} foi comer...") 

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"{self.nome} está miando...")
        
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"{self.nome} está latindo...")
        
class Vaca(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"{self.nome} está mugindo..")
        
class Coelho(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)
    def grunir (self):
        print(f" O {self.nome} está grunindo, iii... iii...")

class Ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprimirvalor(self):
        print(f"O valor do seu ingresso é {self.valor}.")

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor *= 1.5
    def imprimirvalor(self):
        print(f"Seu ingresso VIP custpu {self.valor}")

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def CalArea (self,base,altura):
        self.area = base * altura
        print(self.area)

    def CalPerimetro(self,base,altura):
        self.perimetro = (base + altura) *2

class Triangulo(Forma):

    def __init__(self):
        super().__init__()
    def Calarea (self,base,altura):
        self.area = (base + altura) /2
        print(self.area)
    def CalPerimetro(self,base,altura):
        self.perimetro = (base + altura)
        print(self.perimetro)

class Atleta:
    def __init__(self):
        self.aposentado = False
        self.peso = 0
        self.aquecer = False

    def aposentar(self):
        self.aposentado = True

    def aquecer (self):
        self.aquecer = True

    





















