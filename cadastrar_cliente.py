# biblioteca e funcoes necessarias para que essa parte do programa funcione
import csv
from validar_cadastro import validar_tamanho_cpf, validar_cadastro_cpf


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