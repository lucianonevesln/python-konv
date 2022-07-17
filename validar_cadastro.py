# biblioteca necessaria para que essa parte do programa funcione
import csv


# funcao para validar se a quantidade de caracteres do cpf esta correta
def validar_tamanho_cpf(cpf):
    if len(cpf) != 11:
        print('Digite um numero correto de caracteres para CPF.')
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