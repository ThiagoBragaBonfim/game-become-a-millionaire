from random import randint

def linha(caracter="-",tamanho=30):
    print(caracter*tamanho)


def titulo(texto):
    txt = texto.title()
    print("-"*30)
    print(txt)
    print("-"*30)

def gerar_expressao(tipo):
    num1 = randint(1,31)
    num2 = randint(1,31)
    num3 = randint(1,31)
    num4 = randint(1,5)
    num5 = randint(1,5)

    #Facil
    if tipo == 1:
        expressao = f"{num1} + {num2} - {num3}"
        res = num1 + num2 - num3
        respos = int(input(f"{expressao} = "))

    #medio
    if tipo == 2:
        expressao = f"{num1} * {num4} * {num5}"
        res = num1 * num2 * num3
        respos = int(input(f"{expressao} = "))

    #dificil
    if tipo == 3:
        expressao = f"{num5} ** {num4} + {num3}"
        res = num1 ** num2 + num3
        respos = int(input(f"{expressao} = "))

    #impossivel
    if tipo == 4:
        expressao = f"{num1} ** {num5} * {num4}"
        res = num1 ** num2 * num3
        respos = int(input(f"{expressao} = "))

    return res,respos
