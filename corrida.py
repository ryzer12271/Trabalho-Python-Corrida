
def calcular_categoria(idade):
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
    #retorna -1 se for ínvalido e converte  HH:MM:SS em segundos
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
    # Calcula e retorna o pace
    pace_segundos = segundos // distancia
    minutos = pace_segundos // 60
    segundos_restantes = pace_segundos % 60

    return f"{minutos}'{segundos_restantes:02d}\"/km"


def verificar_premiacao(idade, distancia, segundos):
    # retorna true se o corredor antigir o limite
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


def calcular_resultado():
    

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade >= 16:
                break
            print("Idade invaida e necessário ter 16 anos ou mais")
        except ValueError:
            print("Digite uma idade valida")

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
    print("\n--Menu de cadastrado--")
    print("\n1. Inscrição")
    print("2. Ver cadastro")
    print("3. Calcular resultado")
    print("4. Sair")
    opcao = input("Escolha uma opção: ").strip()
    return opcao


while True:
    opcao = menu_cadastrado()

    if opcao == "1":
        print("Fazer inscrição")
        nome = str(input("Digite seu nome: ")).upper()
        sobrenome = str(input("Digite seu sobrenome: ")).upper()

        while True:
            idade = int(input("qual sua idade: "))
            if idade < 16:
                print("Idade inválida! Tem de ter 16 anos ou mais.")
            else:
                break

        while True:
            print("Qual a distância que você vai percorrer?")
            print("\n1. 5km")
            print("2. 10km")
            distancia = int(input("Escolha uma opcão: "))
            if distancia == 1 or distancia == 2:
                break
            else:
                print("\nInválido!")

        while True:
            print("\nQual seu lote?")
            print("1. Primeiro lote")
            print("2. Segundo lote")
            lote = int(input("Escolha uma opção: "))
            if lote == 1 or lote == 2:
                break
            else:
                print("Inválido!")

        print("\nCadastro realizado com sucesso!")
        print("Retornando ao menu...")

    #ver o cadastro
    elif opcao == "2":
        print("Ver cadastro")

    # calcular o resultado
    elif opcao == "3":
        calcular_resultado()

    elif opcao == "4":
        print("Sair do Sistema")
        break

    else:
        print("Opção invalida!")



