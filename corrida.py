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
#Ver 
    elif opcao == "2":
        print("Ver cadastro") 
         
    
#pede idade, distância e tempo de prova. Mostra os detalhes da corrida incluindo
# o tempo em segundos, o pace e se o competidor foi premiado. 

    elif opcao == "3":
       print("Calcular resultado")

    elif opcao == "4":
       print("Sair do Sistema")

    else:
       print("Opção inválida!")
