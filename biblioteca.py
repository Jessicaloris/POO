class Pessoa():

    def __init__(self, n, i, p):
        self.nome=n
        self.idade=i
        self.peso=p
        self.comendo=False
        self.dormindo=False
        self.falando=False

    def falar(self):
        print(f"{self.nome} começou a falar.")

    def comer(self, comida):
        if self.comendo==True:
            print("Não pode comer, pois já está comendo.")
        print(f"Foi comer {comida}.")

    def dormir(self):
        print(f"{self.nome} foi dormir.")


#parametro n precisa ter o mesmo nome do atributo.
#você pode criar classe e objetos no mesmo arquivo.
