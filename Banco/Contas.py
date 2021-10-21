from abc import ABCMeta, abstractmethod
from Banco.Erros import *
from Banco.Moeda import *

def saque_verboso(objeto, valor):
    print(objeto.nome)
    print(objeto.cpf)
    print(objeto.numero)
    print(objeto.balanco)
    print(objeto.taxa_de_rendimento)
    objeto.saque(valor)
    print(objeto.balanco)

class ContaBancaria (metaclass=ABCMeta):
    """Classe abstrata da conta bancária"""

    quantidade_contas = 0



    @classmethod
    def status_contas(cls):
        return cls.quantidade_contas

    @classmethod
    def incrementa_qtidade_contas(cls):
        cls.quantidade_contas += 1

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def __init__(self, numero, nome, cpf, balanco):

        erro = False

        if numero <0 or numero > 9999:
            raise NumeroDeContaInvalido(numero)
            erro = True
        else:
            self.numero = numero

        if len(nome)>=50:
            raise NomeInvalido(nome)
            erro = True
        else:
            self.nome = nome

        if cpf <0 or cpf > 999_999_999_99:
            raise CPFInvalido(cpf)
            erro = True
        else:
            self.cpf = cpf

        self.balanco = Moeda(balanco)

        if erro == False:
            ContaBancaria.incrementa_qtidade_contas()

    def __str__(self):
        return "A conta de número " + str(self.numero) + " em nome de " + self.nome + " CPF - " + str(self.cpf) + " possui R$ " + str(self.balanco)

    def deposito (self, valor):
        if valor < 0:
            raise ValorMonetarioNegativo(valor)
        else:
            self.balanco = self.balanco + valor
            print ("Depósito de " + str(valor) + " realizado com sucesso.")


    def saque (self, valor):
        if valor < 0:
            raise ValorMonetarioNegativo(valor)
        elif valor > self.balanco:
            raise SaldoInsuficiente(valor)
        else:
            self.balanco = self.balanco - valor
            print ("Saque de " + str(valor) + " realizado com sucesso.")

    @staticmethod
    def saque_verboso(objeto, valor):
        if valor < 0:
            raise ValorMonetarioNegativo(valor)
        elif valor > objeto.saldo:
            raise SaldoInsuficiente(valor)
        else:
            objeto.saldo = objeto.saldo - valor
            print("Saque de " + str(valor) + " realizado com sucesso.")

    @property
    def saldo (self):
        return self.balanco

    @saldo.setter
    def saldo (self, novo_balanco):
        self.balanco = novo_balanco

    @abstractmethod
    def consulta_rendimento (self, dias):
        pass



class ContaCorrente(ContaBancaria):
    quantidade_contas = 0

    @classmethod
    def incrementa_qtidade_contas(cls):
        cls.quantidade_contas += 1

    def __init__(self, numero, nome, cpf, balanco, limite):
        self.taxa_de_rendimento = 0.01
        super().__init__(numero, nome, cpf, balanco)

        # limite precisa ser menor ou igual a zero
        if limite <= 0:
            self.limite=limite
        else:
            raise LimitePrecisaSerNegativo(limite)

        ContaCorrente.incrementa_qtidade_contas()

    def saque (self, valor):
        if valor < 0:
            raise ValorMonetarioNegativo(valor)
        elif valor > (self.balanco + abs(self.limite)):
            raise SaqueAcimaDoLimite(valor)
        else:
            self.balanco = self.balanco - valor
            print ("Saque de " + str(valor) + " realizado com sucesso.")

    def consulta_rendimento (self, dias):
        return ((self.balanco * self.taxa_de_rendimento)/30)*dias

    def __str__(self):
        return super().__str__() + ". É uma conta do tipo Conta Corrente com limite de " + str(self.limite)



class ContaInvestimento(ContaBancaria):
    quantidade_contas = 0

    @classmethod
    def incrementa_qtidade_contas(cls):
        cls.quantidade_contas += 1

    def __init__(self, numero, nome, cpf, balanco, risco):
        super().__init__(numero, nome, cpf, balanco)
        self.risco = risco.strip().lower()
        ContaInvestimento.incrementa_qtidade_contas()

        if risco == "baixo":
            self.taxa_de_rendimento = 0.1
        if risco == "médio" or risco == "medio":
            self.taxa_de_rendimento = 0.25
        if risco == "alto":
            self.taxa_de_rendimento = 0.5



    def consulta_rendimento (self, dias):
        return ((self.balanco * self.taxa_de_rendimento)/30)*dias

    def __str__(self):
        return super().__str__() + ". É uma conta do tipo Conta Investimento com risco " + self.risco



class ContaPoupanca(ContaBancaria):
    quantidade_contas = 0

    @classmethod
    def incrementa_qtidade_contas(cls):
        cls.quantidade_contas += 1

    def __init__(self, numero, nome, cpf, balanco, taxa_de_rendimento):
        super().__init__(numero, nome, cpf, balanco)
        self.taxa_de_rendimento=taxa_de_rendimento
        ContaPoupanca.incrementa_qtidade_contas()


    def consulta_rendimento (self, dias):
        return ((self.balanco * self.taxa_de_rendimento)/30)*dias

    def __str__(self):
        return super().__str__() + ". É uma conta do tipo Conta Poupança com taxa de rendimento de " + str(self.taxa_de_rendimento)
