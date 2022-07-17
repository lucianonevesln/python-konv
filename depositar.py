# bibliotecas e funcao necessarias para que essa parte do programa funcione
import csv
import datetime
from validar_cadastro import validar_cadastro_cpf


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
    else:
        print('\n---------- Operacao cancelada! Digite um CPF valido. ----------\n')