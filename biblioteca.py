"""class Pessoa():
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
            print()"""

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
