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
    """retorna true se o corredor antigir o limite"""
    categoria = calcular_categoria(idade)

    if categoria == "Juvenil":
        limite = 25 * 60 if distancia == 5 else 52 * 60
    elif categoria == "Adulto":
        limite = 22 * 60 if distancia == 5 else 46 * 60
    elif categoria == "Master":
        limite = 25 * 60 if distancia == 5 else 52 * 60
    elif categoria == "Veterano":
        limite = 30 * 60 if distancia == 5 else 63 * 60
    else:
        return False

    return segundos <= limite

def valor_inscricao(lote, distancia):
    """Calcula com base na escolha de lotes o valor que deve se pagar e se haverá acréscimos dependendo da distancia"""
    if lote == 1:
        preco_inicial = 80.00
    elif lote == 2:
        preco_inicial = 100.00
    else:
        preco_inicial = 0.00
    if distancia == 10:
        preco_inicial += 20
    return preco_inicial

#variáveis para armazenar o numero de usuarios e o total de faturamento
total_inscricoes = 0
total_arrecadado = 0.00
def fazer_inscricao():
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
    codigo = nome [0:3] + sobrenome [0:3] + str(idade)
    print("\nCadastro realizado com sucesso!")
    print("Comprovante de registro")
    print(f"Nome do atleta: {nome}")
    print(f"Código: {codigo}")
    print(f"Distancia: {distancia}km")
    print(f"total a se pagar: {valor_inscricao(lote, distancia):.2f}")
    print("Retornando ao menu...")
    return lote, distancia


def calcular_resultado():
    """Pede os dados da prova e do usuário, calcula o desempenho, informa a categoria, a premiação e mostra o resultado final"""
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
        tempo = input("Tempo da prova (HH:MM:SS): ").strip()
        total_segundos = tempo_para_segundos(tempo)

        if total_segundos >= 0:
            break

        print("Tempo invalido! Use HH:MM:SS, por exemplo 00:21:30")

    categoria = calcular_categoria(idade)
    pace = calcular_pace(total_segundos, distancia)
    premiado = verificar_premiacao(idade, distancia, total_segundos)

    print("\n-- Resultado da Corrida --")
    print(f"Categoria: {categoria}")
    print(f"Distancia: {distancia} km")
    print(f"Tempo: {tempo}")
    print(f"Tempo em Segundos: {total_segundos}")
    print(f"Pace: {pace}")

    if premiado:
        print("Premiação: Sim")
    else:
        print("Premiação: Não")

def menu_cadastrado():
    """Exibe o menu principal, recolhe a opção escolhida e retorna o resultado """
    print("\n--Menu de cadastrado--")
    print("\n1. Inscrição")
    print("2. Calcular resultado")
    print("3. Sair")
    opcao = input("Escolha uma opção: ").strip()
    return opcao


while True:
    opcao = menu_cadastrado()
    if opcao == "1":
        lote, distancia = fazer_inscricao()
        total_a_pagar = valor_inscricao(lote, distancia)
        total_inscricoes += 1
        total_arrecadado += total_a_pagar

    #calcular o resultado
    elif opcao == "2":
        calcular_resultado()

    elif opcao == "3":
        print("Sair do Sistema")
        print(f"Total de inscrições: {total_inscricoes}")
        print(f"Total arrecadado: {total_arrecadado}")
        break

    else:
        print("Opção invalida!")



