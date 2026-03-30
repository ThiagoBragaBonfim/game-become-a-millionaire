from classes import Trabalho
from random import randint

custo_trabalho = 100000

nome_trabalhos = [
"Pedreiro","Servente","Eletricista","Encanador","Carpinteiro","Marceneiro","Pintor","Mecânico","Funileiro","Soldador",
"Motorista","Motoboy","Taxista","Caminhoneiro","Piloto","Maquinista","Entregador","Operador de Máquina","Operador de Empilhadeira","Manobrista",
"Padeiro","Confeiteiro","Cozinheiro","Chef","Auxiliar de Cozinha","Garçom","Barman","Barista","Churrasqueiro","Sushiman",
"Atendente","Caixa","Vendedor","Gerente de Loja","Estoquista","Repositor","Fiscal de Loja","Comprador","Representante Comercial","Promotor de Vendas",
"Professor","Professor de Matemática","Professor de História","Professor de Inglês","Coordenador Escolar","Diretor","Monitor Escolar","Tutor","Instrutor","Treinador",
"Médico","Enfermeiro","Técnico de Enfermagem","Dentista","Psicólogo","Fisioterapeuta","Nutricionista","Farmacêutico","Veterinário","Biomédico",
"Recepcionista","Secretário","Assistente Administrativo","Analista Administrativo","Gerente Administrativo","Auxiliar de Escritório","Digitador","Arquivista","Telefonista","Office Boy",
"Advogado","Promotor","Juiz","Delegado","Policial","Bombeiro","Agente Penitenciário","Perito Criminal","Investigador","Segurança",
"Engenheiro Civil","Engenheiro Mecânico","Engenheiro Elétrico","Engenheiro de Produção","Arquiteto","Técnico em Edificações","Topógrafo","Urbanista","Designer de Interiores","Paisagista",
"Programador","Desenvolvedor Web","Analista de Sistemas","Suporte Técnico","Administrador de Redes","Engenheiro de Software","Testador QA","DevOps","Cientista de Dados","Analista de Dados",
"Designer Gráfico","Designer UX","Designer UI","Ilustrador","Fotógrafo","Editor de Vídeo","Animador","Diretor de Arte","Publicitário","Social Media",
"Jornalista","Repórter","Apresentador","Locutor","Roteirista","Produtor","Editor","Crítico","Redator","Copywriter",
"Agricultor","Pecuarista","Agrônomo","Zootecnista","Tratorista","Colhedor","Horticultor","Apicultor","Pescador","Silvicultor",
"Costureiro","Estilista","Modelista","Sapateiro","Joalheiro","Artesão","Ceramista","Escultor","Pintor Artístico","Restaurador",
"Cabeleireiro","Barbeiro","Manicure","Pedicure","Maquiador","Esteticista","Massagista","Terapeuta","Coach","Personal Trainer",
"Garimpeiro","Minerador","Operador de Mina","Geólogo","Técnico em Mineração","Petroleiro","Refinador","Operador de Plataforma","Engenheiro de Petróleo","Sondador",
"Comissário de Bordo","Agente de Viagem","Guia Turístico","Recepcionista de Hotel","Gerente de Hotel","Camareira","Concierge","Agente de Turismo","Organizador de Eventos","Cerimonialista",
"Contador","Auditor","Analista Financeiro","Economista","Tesoureiro","Controlador","Planejador Financeiro","Corretor","Investidor","Caixa Bancário",
"Instrutor de Academia","Treinador de Futebol","Árbitro","Preparador Físico","Nadador Profissional","Jogador de Futebol","Jogador de Basquete","Jogador de Vôlei","Lutador","Treinador Esportivo",
"DJ","Músico","Cantor","Produtor Musical","Compositor","Regente","Técnico de Som","Roadie","Iluminador","Diretor Musical",
"Faxineiro","Zelador","Porteiro","Vigia","Síndico","Jardineiro","Paisagista","Coletor de Lixo","Reciclador","Operador de Limpeza",
"Empresário","Empreendedor","Franqueado","Consultor","Mentor","Diretor Executivo","Gerente Geral","Supervisor","Coordenador","Líder de Equipe",
"Youtuber","Streamer","Influenciador","Criador de Conteúdo","Blogueiro","Podcaster","Editor Digital","Gestor de Comunidade","Moderador","Curador de Conteúdo",
"Detetive Particular","Mágico","Astrólogo","Tarólogo","Guia Espiritual","Pastor","Padre","Missionário","Capelão","Teólogo",
"Bibliotecário","Museólogo","Historiador","Arqueólogo","Antropólogo","Sociólogo","Filósofo","Tradutor","Intérprete","Linguista",
"Operador de Caixa","Frentista","Lavador de Carro","Polidor","Borracheiro","Tapeceiro","Vidraceiro","Gesseiro","Azulejista","Impermeabilizador",
"Entalhador","Lapidador","Ourives","Gravador","Tipógrafo","Impressor","Editor Gráfico","Diagramador","Cartunista","Quadrinista",
"Operador de Telemarketing","Atendente de Call Center","Supervisor de Call Center","Analista de Suporte","Help Desk","Customer Success","Relacionamento com Cliente","Ouvidor","Pesquisador","Entrevistador",
"Alfaiate","Tintureiro","Passador","Costureira Industrial","Designer de Moda","Comprador de Moda","Vendedor de Moda","Gerente de Moda","Consultor de Imagem","Personal Stylist"
]

trabalho_simples = 1500
trabalho_medio = 3000
trabalho_dificil = 6000
trabalho_imposivel = 12000

def gerar_trabalhos(qnt:int = 30):
    trabalhos = []
    repeticao = []
    salarios = [1200, 2500, 5000, 12000, 30000]
    bonus = [200, 500, 1500, 5000, 12000]

    for job in range(qnt):
        numero = randint(0,len(nome_trabalhos)-1)
        while True:
            if numero in repeticao:
                numero = randint(0,len(nome_trabalhos)-1)
            else:
                repeticao.append(numero)
                break
        numero_valor = randint(0,4)
        trabalhos.append(Trabalho(nome_trabalhos[numero],salarios[numero_valor],bonus[numero_valor]))
    return trabalhos

