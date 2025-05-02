saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("""
    Escolha uma opção:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """)
    
    opcao = input("=> ").lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        if valor > saldo:
            print("Saldo insuficiente.")

        elif valor > limite:
            print("Valor acima do limite permitido por saque.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo:   R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Tente novamente.")
