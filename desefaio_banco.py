limite= 500
saldo = 0
extrato = ""
limite_saque = 3

opcao = ""

while opcao !="x":
    opcao = input(
"""----------MENU----------
[s] - SACAR
[d] - DEPOSSITO
[e] - EXTRATO
[q] - SAIR 
: """).lower()
    if opcao == "s" :
        valor = (float(input("Digite o valor que desseja sacar : ")))
        if valor <= 0:
            print("Não é possivel realizar o saque")
        elif saldo <= 0 or saldo < valor:
            print("Não foi possivel realizar o saque por falta de saldo")
        elif limite_saque == 0 :
            print("Limite de saque diario atingido , impossivel realizar o saque")
        elif valor > 500:
            print("Valro do saque superior ao limite permitido , impossivel realizar o saque")
        else:
            saldo -= valor
            limite_saque -= 1
            extrato += f"""-- SAQUE : R${valor:.2f}\n"""
            print("Saque realziado com sucesso!!!\n")
            
    elif opcao == "d":
        valor = (float(input("Digite o valor que desseja depossitar : ")))
        if valor <= 0:
            print("Não é possivel realizar o depossito")
        else:
            saldo += valor
            extrato += f"""++ DEPOSITO : R${valor:.2f}\n"""
            print("Deposito realziado com sucesso!!!\n")

    elif opcao == "e":
        if bool(extrato) == False :
            print("Não foram realizadas movimentações\n")
        print(f"""----EXTRATO-----
{extrato} SALDO : {saldo}""")
        
    elif opcao == "q":
        break
    else:
        print("Opção invalida, porfavafor digite uma opção valida")