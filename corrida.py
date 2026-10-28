TEMPOS_LIMITE = (
    ("Juvenil", 25 * 60, 52 * 60),
    ("Adulto", 22 * 60, 46 * 60),
    ("Master", 25 * 60, 52 * 60),
    ("Veterano", 30 * 60, 63 * 60)
)
def calcular_categoria(idade):
    """Determina com base na idade qual a categoria que o atleta pertence"""
    if idade >= 16 and idade <= 19:
        return "Juvenil"
    elif idade >= 20 and idade <= 39:
        return "Adulto"
    elif idade >= 40 and idade <= 59:
        return "Master"
    elif idade >= 60:
        return "Veterano"
    else:
        return "Idade inválida"


def tempo_para_segundos(tempo):
    """retorna -1 se for ínvalido e converte  HH:MM:SS em segundos"""
    if len(tempo) != 8 or tempo[2] != ":" or tempo[5] != ":":
        return -1

    if not (
        tempo[0:2].isdigit()
        and tempo[3:5].isdigit()
        and tempo[6:8].isdigit()
    ):
        return -1

    horas = int(tempo[0:2])
    minutos = int(tempo[3:5])
    segundos = int(tempo[6:8])

    if minutos > 59 or segundos > 59:
        return -1

    total = horas * 3600 + minutos * 60 + segundos
    return total


def calcular_pace(segundos, distancia):
    """Calcula e retorna o pace"""
    pace_segundos = segundos // distancia
    minutos = pace_segundos // 60
    segundos_restantes = pace_segundos % 60

    return f"{minutos}'{segundos_restantes:02d}\"/km"


def verificar_premiacao(idade, distancia, segundos):
    categoria = calcular_categoria(idade)

    for nome_categoria, limite_5km, limite_10km in TEMPOS_LIMITE:
        if nome_categoria == categoria:
             if distancia == 5:
                limite = limite_5km
             elif distancia == 10:
                limite = limite_10km
             else:
                return False

             return segundos <= limite

    return False

def listar_corredores_com_tempo(corredores):
    """Retorna os corredores que já possuem tempo registrado."""

    corredores_com_tempo = [
        corredor for corredor in corredores
        if corredor["tempo"] is not None
    ]

    for corredor in corredores_com_tempo:
        print(
            f"{corredor['nome']} {corredor['sobrenome']} - "
            f"{corredor['tempo']}"
        )

    if not corredores_com_tempo:
        print("Nenhum corredor possui tempo registrado.")

    return corredores_com_tempo


def listar_corredores_premiados(corredores):
    """Retorna os corredores que atingiram o tempo-limite."""

    corredores_premiados = [
        corredor for corredor in corredores
        if corredor.get("premiado") is True
    ]

    for corredor in corredores_premiados:
        print(
            f"{corredor['nome']} {corredor['sobrenome']} - "
            f"{corredor['categoria']} - "
            f"{corredor['distancia']} km"
        )

    if not corredores_premiados:
        print("Nenhum corredor premiado até o momento.")

    return corredores_premiados


def relatorio_final(corredores, total_inscricoes, total_arrecadado):
    print("\n--- RELATÓRIO FINAL DA CORRIDA ---")
    print(f"Total de inscrições: {total_inscricoes}")
    print(f"Total arrecadado: R${total_arrecadado:.2f}")


    for distancia in(5,10):
        corredores_distancia = [
            corredor for corredor in corredores
            if corredor["distancia"] == distancia
            and corredor.get("tempo_segundos") is not None
        ]

        print(f"\n--- Provas de {distancia} km ---")

        if not corredores_distancia:
            print("Nenhum tempo foi registrado nessa distância")
            continue

        media = sum(
            corredor["tempo_segundos"]
            for corredor in corredores_distancia
        ) / len(corredores_distancia)


        horas = int(media // 3600)
        minutos = int((media % 3600) // 60)
        segundos = int(media % 60)

        print(
           f"Tempo médio "
           f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        )

        mais_rapido = min(
            corredores_distancia,
            key=lambda corredor : corredor["tempo_segundos"]
        )

        print(
            f"Mais rápido: {mais_rapido['nome']}"
            f"{mais_rapido['sobrenome']}"
        )
        print(f"Tempo: {mais_rapido['tempo']}")

        




def valor_inscricao(lote, distancia, idade):
    """Calcula com base na escolha de lotes o valor que deve se pagar e se haverá acréscimos dependendo da distancia"""
    if lote == 1:
        preco_inicial = 80.00
    elif lote == 2:
        preco_inicial = 100.00
    else:
        preco_inicial = 0.00
    if distancia == 10:
        preco_inicial += 20
    if idade >= 60:
        preco_inicial *= 0.5
    return preco_inicial
codigos_usados = set()
def gerar_codigo(nome, sobrenome,idade, codigos_usados):
    """Gera o código do corredor usando as tres primeiras letras do nome, sobrenome e idade"""
    codigo_inicial = nome [0:3] + sobrenome [0:3] + str(idade)
    codigo = codigo_inicial
    numero = 2
    while codigo in codigos_usados:
        codigo = f"{codigo_inicial}--{numero}"
        numero += 1
    return codigo

def contar_categorias(corredores):
    contagem = {
        "Juvenil": 0,
        "Adulto": 0,
        "Master": 0,
        "Veterano": 0,
    }
    for corredor in corredores:
        categoria = corredor["categoria"]
        contagem[categoria] += 1
    return contagem

#variáveis para armazenar o numero de usuarios e o total de faturamento
total_inscricoes = 0
total_arrecadado = 0.00
corredores = []
def fazer_inscricao(codigos_usados):
    """cadastra o usuário e gera um codigo para o corredor além de informar o valor da inscrição"""
    nome = str(input("Digite seu nome: ")).strip().upper()
    sobrenome = str(input("Digite seu sobrenome: ")).strip().upper()
    while True:
        try:
            idade = int(input("qual sua idade: "))
            if idade < 16:
                print("Idade inválida! Tem de ter 16 anos ou mais.")
            else:
                    break
        except ValueError:
            print("Erro: Digite apenas números inteiros.")

    while True:
        try:
            distancia = int(input("Distancia da prova 5 ou 10km: "))
            if distancia == 5 or distancia == 10:
                break
            print("Distancia invalida!")
        except ValueError:
            print("Digite 5 ou 10")

    while True:
        try:
            print("\nQual seu lote?")
            print("1. Primeiro lote")
            print("2. Segundo lote")
            lote = int(input("Escolha uma opção: "))
            if lote == 1 or lote == 2:
                break
            else:
                print("Inválido!")
        except ValueError:
            print("\nDigite os numeros referente as opções!")
    
    total_a_pagar = valor_inscricao(lote,distancia,idade)
    codigo = gerar_codigo(nome, sobrenome, idade, codigos_usados)
    categoria = calcular_categoria(idade)
    print("\nCadastro realizado com sucesso!")
    print("Comprovante de registro")
    print(f"Nome do atleta: {nome}")
    print(f"Código: {codigo}")
    print(f"Categoria: {categoria}")
    print(f"Distancia: {distancia}km")
    print(f"total a se pagar: R${total_a_pagar:.2f}")
    print("Retornando ao menu...")
    
    corredor = {
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade,
            "distancia": distancia,
            "lote": lote,
            "codigo": codigo,
            "categoria": categoria,
            "valor": total_a_pagar,
            "tempo": None
        }
    return corredor


def calcular_resultado():
    #localiza um corredor cadastrado e registra seu resultado

    codigo = input("Digite o código do corredor: ").strip().upper()

    corredor_encontrado = None

    for corredor in corredores:
     if corredor["codigo"] == codigo:
      corredor_encontrado = corredor
      break

    if corredor_encontrado is None:
        print("Erro: corredor não encontrado!")
        return
    while True:
        tempo = input("Tempo da prova (HH:MM:SS): ").strip()
        total_segundos = tempo_para_segundos(tempo)

        if total_segundos >=0:
            break

        print("Tempo inválido! Use HH:MM:SS, exemplo 00:21:30.")

    idade = corredor_encontrado["idade"]
    distancia = corredor_encontrado["distancia"]

    categoria = calcular_categoria(idade)
    pace = calcular_pace(total_segundos, distancia)
    premiado = verificar_premiacao(
        idade, distancia, total_segundos
    )

    #Salva o resultado no cadastro do corredor
    corredor_encontrado["tempo"] = tempo
    corredor_encontrado["tempo_segundos"] = total_segundos
    corredor_encontrado["premiado"] = premiado

    print("\n-- Resultado da Corrida --")
    print(f"Nome: {corredor_encontrado['nome']}")
    print(f"Código: {codigo}")
    print(f"Categoria: {categoria}")
    print(f"Distância: {distancia}km")
    print(f"Tempo: {tempo}")
    print(f"Tempo em segundos: {total_segundos}")
    print(f"Pace{pace}")
    print(f"Premiação: {'Sim' if premiado else 'Não'}")

def listar_inscritos(corredores):
    """Listar todos os corredores cadastrados"""
    if not corredores:
        print("Não tem nenhum corredor cadastrado...")
        return
    for corredor in corredores:
        print(f"\nNome: {corredor['nome']} {corredor['sobrenome']}")
        print(f"Código: {corredor['codigo']}")
        print(f"Categoria: {corredor['categoria']}")
        print(f"Distancia: {corredor['distancia']} km")

def buscar_codigo(corredores):
    """Buscar e encontrar um código e verificar se ele está cadastrado ou não"""
    while True:
        codigo = input("Digite o código que procura: ").strip().upper()
        for corredor in corredores:
            if corredor["codigo"] == codigo:
                print("Corredor encontrado!")
                print(f"\nNome: {corredor['nome']} {corredor['sobrenome']}")
                print(f"Categoria: {corredor['categoria']}")
                print(f"Distancia: {corredor['distancia']} km")
                return corredor
        print("Código não encontrado...")
        continue

def menu_cadastrado():
    """Exibe o menu principal, recolhe a opção escolhida e retorna o resultado """
    print("\n--Menu de cadastrado--")
    print("\n1. Inscrição")
    print("2. Calcular resultado")
    print("3. Lista de corredores")
    print("4. Buscar corredor pelo código")
    print("5. Contagem por categoria")
    print("6. Listar corredores com tempo")
    print("7. Listar corredores premiados")
    print("8. Sair")
    opcao = input("Escolha uma opção: ").strip()
    return opcao


while True:
    opcao = menu_cadastrado()
    if opcao == "1":
        corredor = fazer_inscricao(codigos_usados)
        corredores.append(corredor)
        codigos_usados.add(corredor["codigo"])
        print(corredores)
        total_inscricoes += 1
        total_arrecadado += corredor["valor"]

    #calcular o resultado
    elif opcao == "2":
        calcular_resultado()

    elif opcao == "3":
        listar_inscritos(corredores)

    elif opcao == "4":
        buscar_codigo(corredores)

    elif opcao == "5":
        contagem = contar_categorias(corredores)
        for categoria, quantidade in contagem.items():
            print(f"\n{categoria}: {quantidade} inscritos")
    elif opcao == "6":
        listar_corredores_com_tempo(corredores)


    elif opcao == "7":
        listar_corredores_premiados(corredores)

    elif opcao == "8":
        relatorio_final(
            corredores,
            total_inscricoes,
            total_arrecadado
        )
        print("\nSaindo do Sistema...")

        break

    else:
        print("Opção invalida!")
