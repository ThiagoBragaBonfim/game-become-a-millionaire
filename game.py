from main.classes import *
from main.funcoes import *
from itens.objetos.trabalho import *
from itens.objetos.propiedade import *
from personalizacao import *

ganho_turno = 2000
meta = 10**15



#jogador
quantidade_jogador = 1 #int(input("Informe a quantidade de jogador: "))
saldo_base = 1000000  #(input("Defina um saldo base: "))


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
    if jogador_atual.saldo >= meta:
        print("Você atingiu a meta :) !!!")
        break

    linha()
    print(f"""{cor['azul']}Vez do jogador {jogador_atual.nome}{cor['reset']}
    {cor['verde']}Saldo: 💵R${jogador_atual.saldo}{cor['reset']}
    [1] Loja
    [2] Propiedades Adquiridas
    [3] Dados
    [4] Trabalhos
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
                opc_compra = input(f"{cor['magenta']}Informe o número da propiedade que deseja comprar (digite 'cancelar' para cancelar a compra):{cor['reset']} ")
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

                        # Edu
                        # jogador_atual.atualiza_saldo(propiedade_escolhida.valor)

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

        opc_trabalho = int(input(f"{cor['magenta']}>>> "))

        #Trabalho de ganho imediato
        if opc_trabalho == 1:
            titulo("Trabalho de ganho imediato")
            if trabalho_realizado == False:
                print(f"""
            (1) Trabalho Simples (R${trabalho_simples})
            (2) Trabalho Médio (R${trabalho_medio})
            (3) Trabalho Díficeis (R${trabalho_dificil})
            (4) Trabalho Imposivel (R${trabalho_imposivel})
             """)
                trabalho_realizado = True
                opc_trabalho_imediato = int(input(f"{cor['magenta']}>>> "))
                #trabalho simples
                if opc_trabalho_imediato == 1:
                    titulo("Trabalho Simples")
                    resposta, resposta_jogador = gerar_expressao(1)
                    if resposta_jogador == resposta:
                        jogador_atual.atualizar_saldo(trabalho_simples)
                    else:
                        print(f"A resposta é {resposta}")

                #trabalho medio
                if opc_trabalho_imediato == 2:
                    titulo("Trabalho Médio")
                    resposta, resposta_jogador = gerar_expressao(2)
                    if resposta_jogador == resposta:
                        jogador_atual.atualizar_saldo(trabalho_medio)
                    else:
                        print(f"A resposta é {resposta}")

                #trabalho dificil
                if opc_trabalho_imediato == 3:
                    titulo("Trabalho Difícil")
                    resposta, resposta_jogador = gerar_expressao(3)
                    if resposta_jogador == resposta:
                        jogador_atual.atualizar_saldo(trabalho_dificil)
                    else:
                        print(f"A resposta é {resposta}")

                #trabalho imposivel
                if opc_trabalho_imediato == 4:
                    titulo("Trabalho Impossivel")
                    resposta, resposta_jogador = gerar_expressao(4)
                    if resposta_jogador == resposta:
                        jogador_atual.atualizar_saldo(trabalho_imposivel)
                    else:
                        print(f"A resposta é {resposta}")


            else:
                print(f"{cor['vermelho']}Você já fez um trabalho :)")

        #Trabalho de ganho por turno
        if opc_trabalho == 2:
            titulo("Trabalho de ganho por turno")
            indice = 0
            for job in trabalhos:
                indice += 1
                if job in jogador_atual.trabalhos:
                    print(f"{indice}.{job.nome} (Já contratado)")
                else:
                    print(f"{indice}.{job.nome},Salário: R${job.salario},Bônus; R${job.bonus}")
                linha()
            opc_contrato = int(input(f"{cor['magenta']}Infomer o número do trabalho que deseja (custo de R${custo_trabalho}):{cor['reset']} "))-1
            trabalho_escolhido = trabalhos[opc_contrato]

            if trabalho_escolhido not in jogador_atual.trabalhos:

                if jogador_atual.saldo >= custo_trabalho:
                    jogador_atual.atualizar_saldo(-custo_trabalho)
                    jogador_atual.atualizar_trabalho(1,trabalho_escolhido.salario)
                    jogador_atual.atualizar_trabalho(2,trabalho_escolhido.bonus)
                    jogador_atual.trabalhos.append(trabalho_escolhido)
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
                job.atualizar_rescisao()
        if turno >= len(jogadores):
            turno = 0