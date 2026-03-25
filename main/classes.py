class Jogador:
    def __init__(self,nome,saldo=0,renda=0,renda_trabalho=0,gasto=0,bonus=0):
        self.nome = nome
        self.saldo = saldo
        self.propiedades = []
        self.renda = renda
        self.renda_trabalho = renda_trabalho
        self.trabalhos = []
        self.gasto = gasto
        self.bonus = bonus

    def atualizar_saldo(self,valor):
        self.saldo += valor

    def atualizar_trabalho(self,tipo,valor):
        if tipo == 1:
            self.renda_trabalho += valor
        if tipo == 2:
            self.bonus += valor

class Propiedade:
    def __init__(self,nome,valor,renda,gasto=0):
        self.nome = nome
        self.valor = valor
        self.renda = renda
        self.gasto = gasto


class Trabalho:
    def __init__(self,nome,salario=0,bonus=0,rescisao=0):
        self.nome = nome
        self.salario = salario
        self.rescisao = rescisao
        self.bonus = bonus
    def atualizar_rescisao(self):
        self.rescisao += (self.salario*.1)
        

    