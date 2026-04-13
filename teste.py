pessoas = [
    {'nome': 'thiago', 'idade': 14},
    {'nome': 'ana', 'idade': 20},
    {'nome': 'joao', 'idade': 14},
    {'nome': 'maria', 'idade': 18}
]

idade_procurada = int(input("Digite a idade: "))

for pessoa in pessoas:
    if pessoa['idade'] == idade_procurada:
        print(pessoa['nome'])