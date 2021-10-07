from abc import ABCMeta, abstractmethod
from Erros import *
from Moeda import *

class ContaBancaria (metaclass=ABCMeta):
    """Classe abstrata da conta bancária"""

    quantidade_contas = 0

    @classmethod
    def incrementa_qtidade_contas(cls):
        cls.quantidade_contas += 1

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()

    def __init__(self, numero, nome, cpf, balanco):

        if numero <0 or numero > 9999:
            raise NumeroDeContaInvalido(numero)
        else:
            self.numero = numero

        if len(nome)>=50:
            raise NomeInvalido(nome)
        else:
            self.nome = nome

        if cpf <0 or cpf > 999_999_999_99:
            raise CPFInvalido(cpf)
        else:
            self.cpf = cpf

        self.balanco = balanco
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



    def saldo (self):
        return self.balanco

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
        return super().__str__() + ". É uma conta do tipo Conta Corrente."



class ContaInvestimento(ContaBancaria):
    quantidade_contas = 0

    @classmethod
    def incrementa_qtidade_contas(cls):
        cls.quantidade_contas += 1

    def __init__(self, numero, nome, cpf, balanco, risco):
        super().__init__(numero, nome, cpf, balanco)
        self.risco = risco
        ContaInvestimento.incrementa_qtidade_contas()
        if risco == "baixo":
            self.taxa_de_rendimento = 0.1
        if risco == "médio":
            self.taxa_de_rendimento = 0.25
        if risco == "alto":
            self.taxa_de_rendimento = 0.5



    def consulta_rendimento (self, dias):
        return ((self.balanco * self.taxa_de_rendimento)/30)*dias

    def __str__(self):
        return super().__str__() + ". É uma conta do tipo Conta Investimento."



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
        return super().__str__() + ". É uma conta do tipo Conta Poupança."
