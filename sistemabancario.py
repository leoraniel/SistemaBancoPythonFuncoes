def depositos(deposito,saldo,extrato):
  if deposito > 0:
      saldo += deposito
      extrato += f"DEPOSITO: R${deposito:.2f}\n"
      print("\nDeposito realizado!!!\n")
      print(f"\nNovo Saldo:{saldo}\n")
      return saldo, extrato
  else:
      print("Valor incorreto")




def saques(saque,saldo,extrato):
  if saque > saldo:
      print("Saldo insuficiente")
  else:
      saldo -= saque
      extrato += f"SAQUE: R${saque:.2f}\n"
      print("\nRealizando saque\n")
      print(f"Novo saldo: R${saldo:.2f}")
      return saldo,extrato 



    
def confere_CPF(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
   
   
   
    
def novo_usuario(cpf,usuarios):
  usuario_existente = confere_CPF(cpf,usuarios)
  if usuario_existente:
    print("\nCPF já cadastrado\n")
  else:
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento:  ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})
    
    print("\nCliente cadastrado\n")




def confere_conta(cpf,contas):
  conta_existente = [conta for conta in contas if conta["CPF"] == cpf]
  return conta_existente if conta_existente else None




def nova_conta(cpf,agencia,numero_conta,contas,usuarios):
  usuario_existente = confere_CPF(cpf,usuarios)
  if usuario_existente:
    conta_existente = confere_conta(cpf,contas)
    if conta_existente:
      print("\n------ATENÇÃO ------- \nJá existe uma conta para esse CPF\n")
    else:
      contas.append({"CPF": cpf, "AGÊNCIA" : agencia, "CONTA" : numero_conta})
      print("\nConta cadastrada\n")
  else:
    print("CPF não cadastrado")
 
 
 
  
def listar_contas(contas):
  print("\n CONTAS CADASTRADAS: \n")
  for conta in contas:
    if conta:
      print(f"\nTitular: {conta['CPF']}\nAGÊNCIA: {conta['AGÊNCIA']}\nCONTA: {conta['CONTA']}\n\n")
    else:
      print("Nenhuma conta cadastrada")
      
      
 
 
      
menu ='''
              MENU USUARIO
        S-SAQUE
        D-DEPOSITO
        E-EXTRATO
        NC-NOVA CONTA
        NU-NOVO CLIENTE
        L-LISTAR CONTAS
        q-SAIR      
              
SELECIONE UMA OPÇÃO ACIMA: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_contas = 0
usuarios = []
contas = []


while True:
  opcao = input(menu)
  opcao = opcao.upper()
  
  if opcao == 'D':
    deposito = float(input("Insira valor a ser depositado: "))
    operacao = depositos(deposito,saldo,extrato)
    saldo = int(operacao[0])
    extrato = operacao[1]
  
  elif opcao == 'S':
    if numero_saques >= LIMITE_SAQUES:
      print("Limite de saques excedidos")
    else:
        saque = float(input("Insira valor a ser sacado: "))
        operacao = saques(saque,saldo,extrato)
        saldo = int(operacao[0])
        extrato = operacao[1]
        numero_saques+=1
  
  elif opcao == 'NU':
    cpf = input("Qual o CPF do cliente: ")
    novo_usuario(cpf,usuarios)
    
  elif opcao == 'NC':
    agencia = input("Informe o numero da agência cadastrada: ")
    numero_contas += 1
    cpf = input("Qual o CPF do cliente: ")
    nova_conta(cpf,agencia,numero_contas,contas,usuarios)
 
  elif opcao == 'L':
    listar_contas(contas)   
      
  elif opcao == 'E':
    print(f"Não foram realizadas movimentações.\n" if not extrato else "\n{extrato}" )
    print(f'Saldo: R${saldo:.2f}\n')
  elif opcao == 'Q':
    break
  else:
    print('Opção invalida, Por favor selecione novamente')  
