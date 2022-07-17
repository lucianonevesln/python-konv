# biblioteca e funcao necessarias para que essa parte do programa funcione
import csv
from validar_cadastro import validar_cadastro_cpf


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
    else:
        print('\n---------- # ---------- # ----------\n')