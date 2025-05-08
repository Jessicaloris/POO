"""
conceitos de POO:

* atribuição - São as características de um objeto. Ficam dentro da classe e variam de objeto para objeto.
* métodos - São as ações que o objeto pode fazer. Também ficam dentro da classe.
* objeto - É uma instância (um exemplo real) da classe. Quando você cria um objeto, está criando algo com base no molde da classe.
* mensagem - A comunicação entre objetos.
* classe - É o molde para criar objetos. Define quais atributos (dados) e métodos (ações) o objeto terá.
* abstração - É esconder detalhes complexos e mostrar só o necessário para quem usa o objeto.
* encapsulamento - É o conceito de esconder os detalhes internos do objeto e só permitir o acesso necessário. Protege os dados.
* herança - Permite que uma classe herde características e comportamentos de outra.
* polimorfismo - Permite que métodos com o mesmo nome façam coisas diferentes dependendo da classe. superclasse|subclasse

* Classes - Uma classe define:
Quais atributos os objetos terão (ex: nome, cor, idade).
Quais métodos os objetos poderão executar (ex: andar, falar, buzinar).
Pense na classe como o projeto de uma casa. Você pode usar esse projeto para construir várias casas (objetos),
cada uma com suas cores e móveis (atributos diferentes), mas todas baseadas no mesmo plano.

* Padrão de nomenclatura: Pascal Case - toda primeira letra da cada palavra é sempre maiuscula sem espaços ou sublinhados.
ex:
MinhaClasse
NomeDoArquivo
PessoaFisica


* Metodo construtor em python: __init__
ex de sintaxe básica:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


* self - é uma referência ao próprio objeto dentro da classe.
Quando você cria uma função dentro de uma classe, ela precisa saber qual objeto ela pertence e é ai que entra o self.
ex:
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # 'self.nome' é o atributo da instância

    def dizer_ola(self):
        print(f"Olá, meu nome é {self.nome}")
explicação:
self.nome = nome: associa o valor do argumento nome ao atributo nome da instância.
self.nome: acessa esse valor depois dentro da classe.
Quando você cria uma instância (p = Pessoa("Ana")) e chama p.dizer_ola(), o self automaticamente se refere ao objeto p.

*exercicio 02nj:
  Crie uma classe que tenha os atributos, número da conta, saldo, status da conta (se ela está ativa ou não), nome do cliente
    depositar, sacar verificar saldo e possibilidade de ativar a conta ou desativar a conta. Para desativar uma conta, é necessário
    que o saldo esteja zerado.
"""