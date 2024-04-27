LIMITE= 500
saldo_conta = 0
extrato_conta = ""
limite_saque = 3
clientes = dict()
conta_corrente = dict()

def sacar(*,saldo,valor,extrato,limite,numero_saque):
    if valor <= 0:
            print("Não é possivel realizar o saque")
            return False
    elif valor > limite:
            print("Valro do saque superior ao limite permitido , impossivel realizar o saque")
            return False
    elif saldo <= 0 or saldo < valor:
            print("Não foi possivel realizar o saque por falta de saldo")
            return False
    elif numero_saque == 0 :
            print("Limite de saque diario atingido , impossivel realizar o saque")
            return False
    else:
        saldo -= valor
        extrato += f"""-- SAQUE : R${valor:.2f}\n"""
        print("Saque realziado com sucesso!!!\n")
        return saldo, extrato

def depositar(saldo,valor,extrato,/):
    if valor <= 0:
        print("Não é possivel realizar o depossito")
        return False
    else:
        saldo += valor
        extrato += f"""++ DEPOSITO : R${valor:.2f}\n"""
        print("Deposito realziado com sucesso!!!\n")
        return saldo , extrato

def exibir_extrato(saldo,/,*,extrato):
    if bool(extrato_conta) == False :
        print("Não foram realizadas movimentações\n")
    else:
         print(f"""----EXTRATO-----
{extrato_conta} SALDO : {saldo_conta}""")

def criar_usuario(nome,data_nascimento,cpf,endereco,usuarios):
    if usuarios.items() != None:
        if cpf in usuarios :
            print("Usuário já cadastrado,impossivel realizar o cadastro novamente")
        else:
            adiciona_usuario={f"{cpf}":{'nome':nome, "data_nascimento" :data_nascimento , "endereco" : endereco }}
            usuarios.update(adiciona_usuario)
            print("Usuario cadastrado com sucesso!!!")
    else:
    
        adiciona_usuario={f"{cpf}":{'nome':nome, "data_nascimento" :data_nascimento , "endereco" : endereco }}
        usuarios.update(adiciona_usuario)
        print("Usuario cadastrado com sucesso!!!")

def criar_conta(cpf,conta,cliente):
    AGENCIA = "0001"
    if conta.items() != []:
        if cpf in cliente :
          conta.fromkeys(["agencia","conta_corrente","cpf"])
          numero_conta = conta.get("conta_corrente",0)+ 1
          adicionar_conta = {"agencia" : AGENCIA , "Conta_corrente":numero_conta,"cpf" : cpf}
          conta.update(adicionar_conta)
          print("Conta corrente cadastrada com sucesso")
        else:
            print("Cliente não cadastrado , impossivel abrir conta")
    else:
        numero_conta =  1
        adicionar_conta = {"agencia" : AGENCIA , "conta_corrente":numero_conta , "cpf" : cpf}
        conta.update(adicionar_conta)
        print("Conta corrente cadastrada com sucesso")

def verificar_cliente(cpf,cliente):
    if cpf in cliente:
        return True
    else:
        False


def lista_contas(contas,clientes):
    mensagem = "-----CONTAS CORRENTES-----\n"
    for conta in contas:
        mensagem += f"AGENCIA : {conta["agencia"]} CONTA CORRENTE : {conta["conta_corrente"]}  Tittular : {clientes[conta["cpf"]][0]} \n"
    print(mensagem)

def dados_cliente(cpf,clientes):
    if clientes.items() != None:
        nome_cliente = clientes[f"{cpf}"]["nome"]
        data_nascimento = clientes[f"{cpf}"]["data_nascimento"]
        endereco_cliente = clientes[f"{cpf}"]["endereco"]
        print(f"""
------------DADOS CLIENTE------------
|NOME : {nome_cliente}                  |
|DATA DE NASCIMENTO : {data_nascimento} |
|Endereço : {endereco_cliente} |             
""")
    else:
        print("Cliente não cadastrado!")

opcao = ""

while opcao !="x":
    opcao = input(
"""----------MENU----------
[C] - CRIAR CONTA CORRENTE
[U] - CADASTRAR CLIENTE
[S] - SACAR
[D] - DEPOSSITO
[E] - EXTRATO
[L] - LISTAR CLIENTES
[P] - CONSULTAR DADOS DE CLIENTE
[Q] - SAIR 
: """).lower()
    
    if opcao == "s" :
        valor_saque = (float(input("Digite o valor que desseja sacar : ")))
        aux = sacar(saldo = saldo_conta,valor = valor_saque , extrato = extrato_conta ,limite=LIMITE,numero_saque=limite_saque)
        if aux != False:
            lista_aux = list(aux)
            saldo_conta = float(lista_aux[0])
            extrato_conta = lista_aux[1] 
            limite_saque-=1          
            
    elif opcao == "d":
        valor_depostito = (float(input("Digite o valor que desseja depossitar : ")))
        aux = depositar(saldo_conta,valor_depostito , extrato_conta )
        if aux != False:
            lista_aux = list(aux)
            saldo_conta = lista_aux[0]
            extrato_conta = lista_aux[1]

    elif opcao == "e":
        exibir_extrato(saldo_conta,extrato=extrato_conta)
        
    elif opcao == "q":
        break
    elif opcao == "p":
         cpf_cliente =input("Digite o CPF do cliente : ").replace(".","").replace("-","")
         dados_cliente(cpf=cpf_cliente,clientes=clientes)
    elif opcao == "c":
        cpf_cliente =input("Digite o CPF do cliente : ").replace(".","").replace("-","")
        criar_conta(cpf=cpf_cliente,conta=conta_corrente,cliente=clientes)
    elif opcao == "u":
        nome_cliente=input("Digite o nome do cliente : ")
        data_nascimento_cliente=input("Digite a data de nascimento do cliente : ")
        cpf_cliente =input("Digite o CPF do cliente : ").replace(".","").replace("-","")
        rua = input("Informe o logradouro : ") 
        numero = input("Informe o numerodo da residencia : ")
        bairro = input("Informe o nome do bairro : ")
        cidade = input("Informe o nome da cidade : ")
        uf = input("Informe o UF : ")
        endereco_cliente = f"{rua} n°:{numero} - {bairro} - {cidade}/{uf}"
        criar_usuario(nome=nome_cliente,data_nascimento=data_nascimento_cliente,cpf=cpf_cliente,endereco=endereco_cliente,usuarios=clientes)
    elif opcao == "g":
        lista_contas(conta_corrente,clientes)
    else:
        print("Opção invalida, porfavafor digite uma opção valida")
