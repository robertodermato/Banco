class NumeroDeContaInvalido(Exception):
    """Não são permitidos criar contas com mais que 4 números"""
    def __init__(self,valor):
        self.valor=valor
    def __str__(self):
        return "Contas devem ter 4 dígitos: " + str(self.valor)

class CPFInvalido(Exception):
    """Não são permitidos CPFs inválidos"""
    def __init__(self,valor):
        self.valor=valor
    def __str__(self):
        return "CPFs devem ser números positivos de no máximo 11 dígitos: " + str(self.valor)

class NomeInvalido(Exception):
    """Não são permitidos nomes com maisx de 50 caracteres"""
    def __init__(self,valor):
        self.valor=valor
    def __str__(self):
        return "Nomes devem ter no máximo 50 caracteres: " + str(self.valor)


class LimitePrecisaSerNegativo(Exception):
    """Não são permitidos criar contas com limites positivos"""
    def __init__(self,valor):
        self.valor=valor
    def __str__(self):
        return "Não é possível usar valores positivos para o limite: R$" + str(self.valor)

class ValorMonetarioNegativo(Exception):
    """Não são permitidos transações de valores monetários negativos"""
    def __init__(self,valor):
        self.valor=valor
    def __str__(self):
        return "Não é possível usar valores negativos: R$" + str(self.valor)

class SaldoInsuficiente(Exception):
    """Não é permitido saque maior que o saldo"""
    def __init__(self,valor):
        self.valor=valor
    def __str__(self):
        return "Não é possível sacar R$ " + str(self.valor) + " pois seu saldo é insuficiente."

class SaqueAcimaDoLimite(Exception):
    """Não são permitidos saques acima do limite"""
    def __init__(self,valor):
        self.valor=valor
    def __str__(self):
        return "Não é possível sacar R$ " + str(self.valor) + " pois isso excede seu limite."