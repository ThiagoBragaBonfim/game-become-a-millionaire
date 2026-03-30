#propiedade
from classes import Propiedade
from random import randint

nomes_empresas = [
    "Sol Nascente Padaria",
    "Mercado Boa Vida",
    "Casa do Pão Quente",
    "Açougue do Zé",
    "Lanchonete Sabor Mineiro",
    "Restaurante Dona Maria",
    "Cantina Bela Massa",
    "Churrascaria Fogo & Brasa",
    "Pizzaria Forno Alto",
    "Café Central",

    "Padaria Pão Dourado",
    "Mercadinho Popular",
    "Quitanda Verde Vale",
    "Casa das Carnes Prime",
    "Bistrô Sabor & Arte",
    "Bar da Esquina",
    "Restaurante Sabor Real",
    "Lanchonete Rota 66",
    "Hamburgueria Big Grill",
    "Sorveteria Gelatto",

    "Golden Market",
    "Sunrise Bakery",
    "Green Valley Farm",
    "Happy Burger",
    "Downtown Diner",
    "City Steakhouse",
    "Blue Ocean Café",
    "Family Grocery",
    "Fresh Market Hub",
    "Urban Bistro",

    "Silver Spoon Restaurant",
    "Red Brick Café",
    "Grand Plaza Mall",
    "Central Food Market",
    "Corner Store Express",
    "Happy Kids School",
    "Bright Future School",
    "Elite Training Center",
    "Prime Fitness Gym",
    "Power Fitness Club",

    "Academia Corpo Ativo",
    "Escola Futuro Brilhante",
    "Colégio Nova Geração",
    "Clínica Vida Plena",
    "Hospital Santa Luz",
    "Farmácia Bem Estar",
    "Drogaria Popular",
    "Laboratório Central",
    "Pet Shop Amigo Fiel",
    "Clínica Veterinária Vida Animal",

    "Oficina Auto Center",
    "Mecânica Rápida",
    "Posto Boa Estrada",
    "Posto Gasoline Plus",
    "Lavagem Express",
    "Auto Peças Brasil",
    "Garagem Central",
    "Estacionamento Seguro",
    "Transportadora Rápida",
    "Logística Brasil",

    "Construtora Horizonte",
    "Construtora Nova Era",
    "Materiais ForteLar",
    "Depósito São José",
    "Loja Casa & Obra",
    "Vidraçaria Transparente",
    "Marcenaria Bela Casa",
    "Móveis Planejados Ideal",
    "Decoração Estilo Casa",
    "Design & Lar",

    "Loja Estilo Urbano",
    "Moda Fashion Store",
    "Boutique Elegance",
    "Roupas Boa Vista",
    "Loja Popular Center",
    "Outlet Premium Store",
    "Shopping Center Plaza",
    "Minas Shopping Center",
    "Galeria Central",
    "Centro Comercial União",

    "Cinema Estrela",
    "Teatro Municipal",
    "Parque Verde Vida",
    "Clube Recreativo Sol",
    "Resort Paraíso Azul",
    "Hotel Bela Vista",
    "Pousada Recanto Feliz",
    "Hostel Backpacker Hub",
    "Camping Nature Life",
    "Parque Aquático Splash",

    "Banco União",
    "Banco Popular Brasil",
    "Financeira Crédito Fácil",
    "Investimentos Prime",
    "Seguros Protege Mais",
    "Corretora Confiança",
    "Imobiliária Boa Casa",
    "Imóveis Horizonte",
    "Aluguel Fácil",
    "Casa Própria Já"
]

def gerar_empresas(qnt:int=30):
    propiedades = []
    repeticao = []
    valores = [50000, 120000, 250000, 500000, 900000]
    rendas = [3000, 8000, 18000, 40000, 90000]
    gastos = [1000, 2500, 6000, 15000, 30000]

    for prop in range(qnt):
        numero = randint(0,len(nomes_empresas)-1)
        while True:
            if numero in repeticao:
                numero = randint(0,len(nomes_empresas)-1)
            else:
                repeticao.append(numero)
                break
        numero_valor = randint(0,4)
        propiedades.append(Propiedade(nomes_empresas[numero],valores[numero_valor],rendas[numero_valor],gastos[numero_valor]))

    return propiedades


propiedades = gerar_empresas(10)

