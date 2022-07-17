# bibliotecas e funcao necessarias para que essa parte do programa funcione
import csv
import datetime
from validar_cadastro import validar_cadastro_cpf


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
            if calculo >= 0.0:
                validador = True
                cliente[2] = str(calculo)
        saldo_alterado.append(cliente)
    if validador:
        clientes_saque = open('banco_de_dados_clientes.csv', 'w', newline='')
        clientes_escrita = csv.writer(clientes_saque)
        clientes_escrita.writerows(saldo_alterado)
        clientes_saque.close()
        print('---------- Saque realizado com sucesso! ----------')
    else:
        print('---------- Saldo insulficiente ou CPF nao localizado! ----------')
        clientes_saque.close()
    return validador


# funcao que efetua a atualizacao do saldo
def sacar():
    print('\n---------- # ---------- # ----------\n')
    cpf = str(input('Digite o CPF: '))
    if validar_cadastro_cpf(cpf) == False:
        print('Escolha uma das opcoes abaixo: \n1.00; \n2.00; \n5.00; \n10.00; \n20.00; \n50.00; \n100.00; \n')
        valor = float(input('Digite o valor para saque: '))
        print('\n---------- # ---------- # ----------\n')
        if valor in [1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00]:
            if sacar_valor(cpf, valor) == True:
                natureza = 'Saida'
                hora_agora = datetime.datetime.now()
                nova_operacao = [hora_agora, cpf, natureza, valor]
                with open('banco_de_dados_operacoes.csv', mode='a+', newline='') as operacoes:
                    operacao = csv.writer(operacoes)
                    operacao.writerow(nova_operacao)
        else:
            print('\nEscolha a opcao de saque e digite o valor correto.\n')
    else:
        print('\n---------- Operacao cancelada! Digite um CPF valido. ----------\n')