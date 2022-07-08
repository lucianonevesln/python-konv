# bibliotecas necessarias
import csv
import datetime


# funcao para validar se a quantidade de caracteres do cpf esta correta
def validar_tamanho_cpf(cpf):
    if len(cpf) != 11:
        print('Digite um numero correto de caracteres.')
    else:
        return True


# funcao para validar se o cliente ja possui cadastro
def validar_cadastro_cpf(cpf):
    retorno = True
    with open('banco_de_dados_clientes.csv', mode='r') as clientes_validar:
        validar = csv.reader(clientes_validar, delimiter=',')
        for cliente in validar:
            if cpf == cliente[0]:
                print('\nCliente ja cadastrado. Se deseja efetuar um um novo cadastro, escolha essa opção no menu.')
                print('Se estiver efetuando depósito, saque ou consultando extrato, desconsidere a mensagem.\n')
                retorno = False
    return retorno


# funcao que efetua o calculo do deposito
def depositar_valor(cpf, valor):
    clientes_deposito = open('banco_de_dados_clientes.csv', 'r', newline='\n')
    validador = False
    clientes_leitura = csv.reader(clientes_deposito)
    saldo_alterado = []
    for cliente in clientes_leitura:
        if cliente[0] == cpf:
            calculo = float(cliente[2])
            calculo += valor
            cliente[2] = str(calculo)
            validador = True
        saldo_alterado.append(cliente)
    if validador:
        clientes_deposito = open('banco_de_dados_clientes.csv', 'w', newline='')
        clientes_escrita = csv.writer(clientes_deposito)
        clientes_escrita.writerows(saldo_alterado)
        clientes_deposito.close()
        print('---------- Depósito realizado com sucesso! ----------')
    else:
        print('---------- CPF nao localizado! ----------')
        clientes_deposito.close()


# funcao que efetua a atualizacao do saldo
def depositar():
    print('\n---------- # ---------- # ----------\n')
    cpf = str(input('Digite o CPF: '))
    if validar_cadastro_cpf(cpf) == False:
        valor = float(input('Digite o valor para depósito: '))
        print('\n---------- # ---------- # ----------\n')
        depositar_valor(cpf, valor)
        natureza = 'Entrada'
        hora_agora = datetime.datetime.now()
        nova_operacao = [hora_agora, cpf, natureza, valor]
        with open('banco_de_dados_operacoes.csv', mode='a+', newline='') as operacoes:
            operacao = csv.writer(operacoes)
            operacao.writerow(nova_operacao)
        menu()
    else:
        print('\n---------- Operacao cancelada! Digite um CPF valido. ----------\n')
        menu()


# funcao que efetua o calculo do saque
def sacar_valor(cpf, valor):
    clientes_saque = open('banco_de_dados_clientes.csv', 'r', newline='\n')
    validador = False
    clientes_leitura = csv.reader(clientes_saque)
    saldo_alterado = []
    for cliente in clientes_leitura:
        if cliente[0] == cpf:
            calculo = float(cliente[2])
            calculo -= valor
            cliente[2] = str(calculo)
            validador = True
        saldo_alterado.append(cliente)
    if validador:
        clientes_saque = open('banco_de_dados_clientes.csv', 'w', newline='')
        clientes_escrita = csv.writer(clientes_saque)
        clientes_escrita.writerows(saldo_alterado)
        clientes_saque.close()
        print('---------- Saque realizado com sucesso! ----------')
    else:
        print('---------- CPF nao localizado! ----------')
        clientes_saque.close()


# funcao que efetua a atualizacao do saldo
def sacar():
    print('\n---------- # ---------- # ----------\n')
    cpf = str(input('Digite o CPF: '))
    if validar_cadastro_cpf(cpf) == False:
        print('Escolha uma das opcoes abaixo: \n1.00; \n2.00; \n5.00; \n10.00; \n20.00; \n50.00; \n100.00; \n')
        valor = float(input('Digite o valor para saque: '))
        print('\n---------- # ---------- # ----------\n')
        if valor in [1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00]:
            sacar_valor(cpf, valor)
            natureza = 'Saida'
            hora_agora = datetime.datetime.now()
            nova_operacao = [hora_agora, cpf, natureza, valor]
            with open('banco_de_dados_operacoes.csv', mode='a+', newline='') as operacoes:
                operacao = csv.writer(operacoes)
                operacao.writerow(nova_operacao)
            menu()
        else:
            print('\nEscolha a opcao de saque e digite o valor correto.\n')
            menu()
    else:
        print('\n---------- Operacao cancelada! Digite um CPF valido. ----------\n')
        menu()


# funcao que cadastra um novo cliente
def cadastrar_cliente():
    print('\n---------- # ---------- # ----------\n')
    nome = str(input('Digite o nome: '))
    cpf = str(input('Digite o CPF: '))
    limite_concedido = 0.00
    print('\n---------- # ---------- # ----------\n')
    if validar_tamanho_cpf(cpf) and validar_cadastro_cpf(cpf):
        novo_cadastro = [cpf, nome, limite_concedido]
        with open('banco_de_dados_clientes.csv', mode='a+', newline='') as clientes:
            cliente = csv.writer(clientes)
            cliente.writerow(novo_cadastro)
            print('Cliente: {} - CPF: {}, cadastrado(a) com sucesso!'.format(nome, cpf))
    menu()


# funcao que lista todos os clientes cadastrados
def listar_clientes():
    with open('banco_de_dados_clientes.csv', mode='r') as clientes_cadastrados:
        leitura = csv.reader(clientes_cadastrados, delimiter=',')
        contador = 0
        for cliente in leitura:
            if contador == 0:
                print('\n---------- Lista de Clientes ----------\n')
                print(f'Cabecalho: {" ".join(cliente)}')
                contador += 1
            else:
                print(f'Cliente: {" ".join(cliente)}')
                contador += 1
    menu()


# funcao que apresenta extrato com o saldo final
def consultar_extrato_saldo():
    print('\n---------- # ---------- # ----------\n')
    cpf = str(input('Digite o CPF: '))
    if validar_cadastro_cpf(cpf) == False:
        print('\n---------- # ---------- # ----------\n')
        print('Extrato')
        print(['Data', 'CPF', 'Entrada/Saida', 'Valor'])
        with open('banco_de_dados_operacoes.csv', mode='r') as operacoes_cadastradas:
            leitura = csv.reader(operacoes_cadastradas, delimiter=',')
            for operacao in leitura:
                if operacao[1] == cpf:
                    print(operacao)
        with open('banco_de_dados_clientes.csv', mode='r') as clientes_cadastrados:
            leitura = csv.reader(clientes_cadastrados, delimiter=',')
            for cliente in leitura:
                if cliente[0] == cpf:
                    print('O(a) cliente: {}, possui saldo final de: {}.'.format(cliente[1], cliente[2]))
        menu()
    else:
        print('\n---------- # ---------- # ----------\n')
        menu()


# funcao que apresenta opcoes para usuario interagir com o sistema
def menu():
    print('\n---------- Menu de Opcoes ----------\n')
    print('Digite 1 para: Cadastrar um novo cliente')
    print('Digite 2 para: Listar Clientes Existentes')
    print('Digite 3 para: Realizar Depósito')
    print('Digite 4 para: Realizar Saque')
    print('Digite 5 para: Consultar Extrato/Saldo')
    print('Digite 6 para: Sair do Sistema')
    print('\n---------- Fim Menu ----------\n')
    opcao = int(input("Digite a opcao escolhida: "))
    if opcao == 1:
        cadastrar_cliente()
    elif opcao == 2:
        listar_clientes()
    elif opcao == 3:
        depositar()
    elif opcao == 4:
        sacar()
    elif opcao == 5:
        consultar_extrato_saldo()
    elif opcao == 6:
        print('\n---------- Saindo do sistema... ----------\n')
    else:
        print('\n---------- Escolha uma opcao valida. ----------\n')
        menu()


# chamada para execucao do sistema
menu()