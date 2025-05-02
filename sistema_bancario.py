def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")

    elif valor > limite:
        print("Valor acima do limite permitido por saque.")

    elif numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Valor inválido para saque.")

    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
   
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido para depósito.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
   
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo:   R$ {saldo:.2f}")
    print("==============================")

def cadastrar_usuario(usuarios):
  
    cpf = input("Informe o CPF (somente números): ")
    usuario = [u for u in usuarios if u["cpf"] == cpf]

    if usuario:
        print("Usuário já existe!")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")

def cadastrar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = [u for u in usuarios if u["cpf"] == cpf]

    if not usuario:
        print("Usuário não encontrado! Cadastre antes.")
        return None

    print("Conta criada com sucesso!")
    return {"agencia": agencia, "numero": numero_conta, "usuario": usuario[0]}

def menu():
    print("""
    Escolha uma opção:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [q] Sair
    """)
    return input("=> ").lower()

# Programa principal
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

AGENCIA = "0001"

while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        cadastrar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Tente novamente.")
