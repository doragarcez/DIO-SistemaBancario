#V.1 Desafio DIO - Sistema Bancário

saldo = 0
limite = 500
numero_saque = 0
extrato = []
LIMITE_SAQUES = 3
menu = """
\n===================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
===================\n
=> """

while True:
    opcao = input(menu)

    match opcao:
        case "1":
            valor = float(input("O quanto deseja depositar?"))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print("Depósito realizado com sucesso!")
            else:
                print("Valor inválido. Tente novamente.")
        case "2":
            if numero_saque < LIMITE_SAQUES:
                valor = float(input("Quanto deseja sacar?"))
                if 0 < valor <= saldo and valor <= limite:
                    saldo -= valor
                    numero_saque += 1
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    print("Saque realizado com sucesso!")
                else:
                    print("Valor inválido ou fora do limite permitido.")
            else:
                print("Limite de saques diários atingido. Tente novamente amanhã.")
        case "3":
            print("\n========== EXTRATO ==========")
            if extrato:
                for transacao in extrato:
                    print(transacao)
            else:
                print("Não foram realizadas movimentações.")
                print(f"Saldo atual: R$ {saldo:.2f}")
                print("==============================\n")
        case "4":
            print("Obrigada por utilizar o Banco Y. Até logo!")
            break
        case _:
            print("Opção inválida. Tente novamente.")

