class Moeda:
    """Classe da moeda"""
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

    def __add__(self, outro):
        if isinstance(outro, float):
            novo_valor = self.valor + outro
        elif isinstance(outro, int):
            novo_valor = self.valor + outro
        else:
            novo_valor = self.valor + outro.valor
        return novo_valor

    def __iadd__(self, outro):
        if isinstance(outro, float):
            self.valor += outro
        else:
            self.valor += outro.valor
        return self.valor

    def __sub__(self, outro):
        if isinstance(outro, float):
            novo_valor = self.valor - outro
        elif isinstance(outro, int):
            novo_valor = self.valor - outro
        else:
            novo_valor = self.valor - outro.valor
        return novo_valor

    def __isub__(self, outro):
        if isinstance(outro, float):
            self.valor -= outro
        else:
            self.valor -= outro.valor
        return self.valor

    def __mul__(self, outro):
        if isinstance(outro, float):
            novo_valor = self.valor * outro
        else:
            novo_valor = self.valor * outro.valor
        return novo_valor

    def __imul__(self, outro):
        if isinstance(outro, float):
            self.valor *= outro
        else:
            self.valor *= outro.valor
        return self.valor

    def __truediv__(self, outro):
        if isinstance(outro, float):
            novo_valor = self.valor / outro
        else:
            novo_valor = self.valor / outro.valor
        return novo_valor

    def __idiv__(self, outro):
        if isinstance(outro, float):
            self.valor /= outro
        else:
            self.valor /= outro.valor
        return self.valor

    def __eq__(self, outro):
        if isinstance(outro, float):
            return self.valor == outro
        else:
            return self.valor == outro.valor

    def __ne__(self, outro):
        if isinstance(outro, float):
            return self.valor != outro
        else:
            return self.valor != outro.valor

    def __lt__(self, outro):
        if isinstance(outro, float):
            return self.valor < outro
        else:
            return self.valor < outro.valor

    def __gt__(self, outro):
        if isinstance(outro, float):
            return self.valor > outro
        else:
            return self.valor > outro.valor

    def __ge__(self, outro):
        if isinstance(outro, float):
            return self.valor >= outro
        else:
            return self.valor >= outro.valor