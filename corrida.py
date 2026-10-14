def menu_cadastrado():
    print("--Menu de cadastrado--")
    print("\n1. Inscrição")
    print("2. Ver cadastro")
    print("3. Sair")
    opcao = input("Escolha uma opção: ").strip()
    return opcao
while True:
    opcao = menu_cadastrado()

    if opcao == "1":
     print("Fazer inscrição")

    elif opcao == "2":
       print("Calcular resultado")

    elif opcao == "3":
       print("Sair do Sistema")

    else:
       print("Opção inválida!")
