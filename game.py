from random import  randint
from colorama import init,Fore

init(autoreset=True)

cor = {
    'verde' : Fore.GREEN,
    'vermelho' : Fore.RED,
    'amarelo' : Fore.YELLOW,
    'azul' :  Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'reset' :  Fore.RESET,
       }

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






def linha(caracter="-",tamanho=30):
    print(caracter*tamanho)

def titulo(texto):
    txt = texto.title()
    print("-"*30)
    print(txt)
    print("-"*30)

ganho_turno = 2000

trabalho_simples = 1500
trabalho_medio = 3000
trabalho_dificil = 6000
trabalho_imposivel = 12000


#jogador
quantidade_jogador = 1 #int(input("Informe a quantidade de jogador: "))

saldo_base = 0  #(input("Defina um saldo base: "))

#propiedade
cafeteria = Propiedade("Cafeteria",80000,5000,2000)
bar = Propiedade("Bar do Branco",45000,3500,1200)
lanchonete = Propiedade("Lanchonete",150000,8500,6000)
escola = Propiedade("Escola",480000,85000,35000)
shopping1 = Propiedade("Minas Shopping",800000,280000,58000)
shopping2 = Propiedade("Del Rey",650000,150000,36000)

propiedades = [cafeteria,bar,lanchonete,escola,shopping1,shopping2]

#Trabalho
custo_trabalho = 100000

vendedor =  Trabalho("Vendendor",3000,300)
diretor =  Trabalho("Diretor",6000,100)
uber =  Trabalho("Uber",1000,10,)
professor =  Trabalho("Professor",5000,500)
barista =  Trabalho("Barista",4500,350)

trabalhos = [vendedor,diretor,uber,professor,barista]





#jogadores (def)
jogadores = []

for i in range(quantidade_jogador):
    nome_jogador =  "Thiago" #input(f"Informe o nome do jogador {i+1}: ").title()
    jogador = Jogador(nome_jogador,saldo_base)
    jogadores.append(jogador)

turno = 0

trabalho_realizado = False

#jogo
while True:
    chance_bonus = randint(1, 10)
    chance_rescisao = randint(1,4)
    jogador_atual = jogadores[turno]
    linha()
    print(f"""{cor['azul']}Vez do jogador {jogador_atual.nome}{cor['reset']}
    {cor['verde']}Saldo: 💵R${jogador_atual.saldo}{cor['reset']}
    [1] Loja
    [2] Propiedades Adquiridas
    [3] Dados
    [4] Trabalhos (em dev)
    [0] Pular
""")
    opc = int(input(f"{cor['magenta']}>>> "))
    linha()

    #loja
    if opc == 1:
        titulo("Loja")
        linha()
        indice = 0

        if len(jogador_atual.propiedades) < len(propiedades):
            for propiedade in propiedades:

                if propiedade in jogador_atual.propiedades:
                    print(f"{indice}.{propiedade.nome} (adquirido) ")
                else:
                    print(f"{indice}.{propiedade.nome}|Valor: R${propiedade.valor}|Renda: R${propiedade.renda}|Custo por turno: R${propiedade.gasto}")
                linha("-",20)
                indice += 1
            while True:
                opc_compra = input(f"{cor['magenta']}Informe o número da propiedade que deseja comprar (digite 'cancelar' para cancelar a compra): ")
                if opc_compra.lower() == 'cancelar':
                    print(f"{cor['vermelho']}Compra cancelada")
                    linha()
                    break
                else:
                    opc_compra = int(opc_compra)
                propiedade_escolhida = propiedades[opc_compra]


                if propiedade_escolhida not in jogador_atual.propiedades:

                    if jogador_atual.saldo >= propiedade_escolhida.valor:

                        jogador_atual.saldo -= propiedade_escolhida.valor
                        jogador_atual.propiedades.append(propiedade_escolhida)
                        jogador_atual.renda += propiedade_escolhida.renda
                        jogador_atual.gasto += propiedade_escolhida.gasto
                        print( f"Propiedade {cor['azul']}{propiedade_escolhida.nome}{cor['reset']} foi comprada com sucesso!!!")
                        linha()
                        break

                    else:
                        print(f"{cor['vermelho']}Saldo insuficiente")

                else:
                    print(f"{cor['vermelho']}Propiedade já adquirida")

        else:
            print("Você Possui todas as propiedades :) !!!")

    #propiedades adquiridas
    if opc == 2:
        titulo("Propiedades Adquiridas")
        indice = 0
        if len(jogador_atual.propiedades) > 0:
            for prop in jogador_atual.propiedades:
                indice += 1
                print(f"{indice}.{prop.nome}")
        else:
            print(f"{cor['vermelho']}Você não possui nenhuma propiedade ainda :(")

    #dados
    if opc == 3:
        titulo("Dados")
        print(f"""{cor['verde']}
    -Renda: 💵R${jogador_atual.renda}
    -Gastos: 💵R${jogador_atual.gasto}
    -Renda (trabalhos): 💵R${jogador_atual.renda_trabalho} 
    -Bônus: 💵R${jogador_atual.bonus}
    -Ganho por turno : 💵R${ganho_turno+(jogador_atual.renda - jogador_atual.gasto)+jogador_atual.renda_trabalho}""")
        linha()
        if len(jogador_atual.trabalhos) > 0:
            indice = 0
            print("Trabalhos:")
            for job in jogador_atual.trabalhos:
                indice += 1
                print(f"{indice}.{job.nome}| Rescisão: 💵R${job.rescisao}")
            linha()




    #trabalhos
    if opc == 4:
        titulo("Trabalho")

        print("""
    [1] Trabalho de ganho imediato
    [2] Trabalho de ganho por turno
    [3] Demissão
        """)

        #Trabalho de ganho imediato
        opc_trabalho = int(input(f"{cor['magenta']}>>> "))

        if opc_trabalho == 1:
            titulo("Trabalho de ganho imediato")
            if trabalho_realizado == False:
                print(f"""
            (1) Trabalho Simples (R${trabalho_simples})
            (2) Trabalho Médio (R${trabalho_medio})
            (3) Trabalho Díficeis (R${trabalho_dificil})
            (4) Trabalho Imposivel (R${trabalho_imposivel})
             """)
                opc_trabalho = int(input(f"{cor['magenta']}>>> "))

                #trabalho simples
                if opc_trabalho == 1:
                    titulo("Trabalho Simples")
                    num1 = randint(0,31)
                    num2 = randint(0,31)
                    num3 = randint(0,31)
                    expressao = num1 + num2 - num3
                    print(f"{num1} + {num2} - {num3}")
                    resposta = int(input(f"{cor['magenta']}>>> "))
                    if resposta == expressao:
                        print("Você acertou :)!!!")
                        jogador_atual.saldo += trabalho_simples
                        trabalho_realizado = True
                    else:
                        print(f"{cor['vermelho']}Você errou :(, a resposta é {expressao}")

                #trabalho medio
                if opc_trabalho == 2:
                    titulo("Trabalho Médio")
                    num1 = randint(0,11)
                    num2 = randint(0,11)
                    num3 = randint(0,31)
                    num4 = randint(0,31)
                    num5 = randint(0,31)
                    expressao = num1 * num2 + (num3 + num4 + num5)
                    print(f"{num1} * {num2} + ({num3} + {num4} + {num5})")
                    resposta = int(input(f"{cor['magenta']}>>> "))
                    if resposta == expressao:
                        print("Você acertou :)!!!")
                        jogador_atual.saldo += trabalho_medio
                        trabalho_realizado = True
                    else:
                        print(f"{cor['vermelho']}Você errou :(, a resposta é {expressao}")

                #trabalho dificil
                if opc_trabalho == 3:
                    titulo("Trabalho Difícil")
                    num1 = randint(0,6)
                    num2 = randint(0,4)
                    num3 = randint(0,31)
                    num4 = randint(0,31)
                    num5 = randint(0,31)
                    expressao = num1 ** num2 + (num3 + num4 + num5)
                    print(f"{num1} ** {num2} + ({num3} + {num4} + {num5})")
                    resposta = int(input(f"{cor['magenta']}>>> "))
                    if resposta == expressao:
                        print("Você acertou :)!!!")
                        jogador_atual.saldo += trabalho_dificil
                        trabalho_realizado = True
                    else:
                        print(f"{cor['vermelho']}Você errou :(, a resposta é {expressao}")

                #trabalho imposivel
                if opc_trabalho == 4:
                    titulo("Trabalho Impossivel")
                    num1 = randint(0,11)
                    num2 = randint(0,11)
                    num3 = randint(0,31)
                    num4 = randint(0,31)
                    num5 = randint(0,31)
                    expressao = num1 ** num2 * (num3 + (num4 + num5))
                    print(f"{num1} ** {num2} * ({num3} + ({num4} + {num5})")
                    resposta = int(input(f"{cor['magenta']}>>> "))
                    if resposta == expressao:
                        print("Você acertou :)!!!")
                        jogador_atual.saldo += trabalho_imposivel
                        trabalho_realizado = True
                    else:
                        print(f"{cor['vermelho']}Você errou :(, a resposta é {expressao}")



            else:
                print(f"{cor['vermelho']}Você já fez um trabalho :)")

        #Trabalho de ganho por turno
        if opc_trabalho == 2:
            titulo("Trabalho de ganho por turno")
            indice = 0
            for job in trabalhos:
                indice += 1
                print(f"{indice}.{job.nome},Salário: R${job.salario},Bônus; R${job.bonus}")
                linha()
            opc_contrato = int(input(f"{cor['magenta']}Infomer o número do trabalho que deseja (custo de R${custo_trabalho}): "))-1
            trabalho_escolhido = trabalhos[opc_contrato]

            if trabalho_escolhido not in jogador_atual.trabalhos:

                if jogador_atual.saldo >= custo_trabalho:
                    jogador_atual.saldo -= custo_trabalho
                    jogador_atual.renda_trabalho += trabalho_escolhido.salario
                    jogador_atual.trabalhos.append(trabalho_escolhido)
                    jogador_atual.bonus += trabalho_escolhido.bonus
                    print(f"Você foi contratado com o cargo de {cor['azul']}{trabalho_escolhido.nome}{cor['reset']} :)!")

                else:
                    print(f"{cor['vermelho']}Saldo Insuficiente :(")

            else:
                print(f"{cor['vermelho']}Você já esta contratado neste local :) ")



        #Demissão
        if opc_trabalho == 3:
            titulo("demissão")

            if len(jogador_atual.trabalhos) > 0:
                indice = 0

                for job in jogador_atual.trabalhos:
                    indice += 1
                    print(f"{indice}.{job.nome}")
                opc_demissao = int(input(">>> "))-1
                demissao_escolhida = jogador_atual.trabalhos[opc_demissao]

                if chance_rescisao == 1:
                    jogador_atual.saldo += demissao_escolhida.rescisao
                    print(f"{cor['verde']}Você ganhou a rescisão!!!")

                else:
                    print(f"{cor['vermelho']}Você não ganhou a rescisão")

                jogador_atual.trabalhos.remove(demissao_escolhida)


            else:
                print(f"{cor['vermelho']}Você não tem nenhum trabalho")

    #pular
    if opc == 0:
        titulo("Pular")
        turno += 1
        jogador_atual.saldo += (ganho_turno + (jogador_atual.renda - jogador_atual.gasto) + jogador_atual.renda_trabalho)
        trabalho_realizado = False
        if len(jogador_atual.trabalhos) > 0:
            if chance_bonus == 1:
                print("Você ganhou o bônus do trabalho !!! :)")
                for job in jogador_atual.trabalhos:
                    jogador_atual.saldo += job.bonus

            for job in jogador_atual.trabalhos:
                job.rescisao += (job.salario * .1)
        if turno >= len(jogadores):
            turno = 0