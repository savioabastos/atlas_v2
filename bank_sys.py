def deposito(saldo_atual, valor_deposito, extrato_atual):
    if valor_deposito <= 0:
        print("\nValor de depósito inválido")
    else:
        saldo_atual += valor_deposito
        extrato_atual += f"+ {valor_deposito:.2f}R$\n"
        
    return saldo_atual, extrato_atual

def saque(saldo_atual, valor_saque, extrato_atual, limite_saque, numero_saques_atual, limite_saques_diario):
    saldo_excedido = valor_saque > saldo_atual
    limite_excedido = valor_saque > limite_saque
    saques_excedidos = numero_saques_atual >= limite_saques_diario
    
    if saldo_excedido:
        print("O valor do saque excedeu o valor do saldo atual da conta")
    elif limite_excedido:
        print("O valor do saque excedeu o limite atual")
    elif saques_excedidos:
        print("Número máximo de saques excedido")
    elif valor_saque > 0:
        saldo_atual -= valor_saque
        extrato_atual += f"- {valor_saque:.2f}R$\n"
        numero_saques_atual += 1
        print("Saque realizado com sucesso")
    else:
        print("Formato inválido")
    
    return saldo_atual, extrato_atual, numero_saques_atual

def exibir_extrato(saldo_atual, extrato_atual):
    print('_____EXTRATO____')
    if not extrato_atual:
        print("Não houve movimentações na conta.")
    else:
        print(extrato_atual)
    print(f"Saldo: {saldo_atual:.2f}R$")
    print('________________')

def filtrar_usuario(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_usuario(lista_usuarios):
    cpf = input("Informe seu CPF: ")
    usuario_existente = filtrar_usuario(cpf, lista_usuarios)
    if usuario_existente:
        print("\nJá existe um usuário cadastrado com este CPF.")
        return
    nome_completo = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco_completo = input("Informe o endereço: ")
    lista_usuarios.append({"nome": nome_completo, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco_completo})

def cadastrar_conta_bancaria(agencia_bancaria, numero_conta, lista_usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario_existente = filtrar_usuario(cpf, lista_usuarios)
    if usuario_existente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia_bancaria, "numero_conta": numero_conta, "usuario": usuario_existente}

def input_command():
    menu = '''
    [D]\tDEPOSITAR
    [S]\tSACAR
    [E]\tEXTRATO
    [NA]\tCADASTRAR NOVA CONTA
    [NU]\tCADASTRAR NOVO USUÁRIO
    [Q]\tSAIR
    =>
    '''
    return input(menu).strip().upper()

def main():
    LIMITE_SAQUES_DIARIO = 3
    AGENCIA_BANCARIA = "0001"

    saldo_atual = 0
    limite_saque = 500
    extrato_atual = ""
    numero_saques_atual = 0
    lista_usuarios = []
    lista_contas = []
    
    while True:
        comando = input_command()
        
        if comando == 'D':
            valor_deposito = float(input("Informe o valor do depósito: "))
            saldo_atual, extrato_atual = deposito(saldo_atual, valor_deposito, extrato_atual)
            
        elif comando == 'S':
            valor_saque = float(input("Informe o valor do saque: "))
            saldo_atual, extrato_atual, numero_saques_atual = saque(
                saldo_atual=saldo_atual,
                valor_saque=valor_saque,
                extrato_atual=extrato_atual,
                limite_saque=limite_saque,
                numero_saques_atual=numero_saques_atual,
                limite_saques_diario=LIMITE_SAQUES_DIARIO
            )
            
        elif comando == 'E':
            exibir_extrato(saldo_atual, extrato_atual)
            
        elif comando == 'NA':
            numero_conta = len(lista_contas) + 1
            conta = cadastrar_conta_bancaria(AGENCIA_BANCARIA, numero_conta, lista_usuarios)
            if conta:
                lista_contas.append(conta)
            
        elif comando == 'NU':
            cadastrar_usuario(lista_usuarios)
            
        elif comando == 'Q':
            print('Encerrando...')
            break
        else:
            print('Comando não identificado')

main()
